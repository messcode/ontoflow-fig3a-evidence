import json,uuid,time,requests,os
from pathlib import Path
from http.server import BaseHTTPRequestHandler
from compat import local_tools, output_allowance
from context_budget import fit_tool_history, digest
ROOT=Path('/mnt/disk3/chzhang/fr24-qwen-evidence-ZxEGe9/hardware')

def prepare_chat(session, endpoint, chat):
 def post(route, body):
  response=session.post(endpoint+route,json=body,timeout=(8,120))
  response.raise_for_status()
  return response.json()
 def count(item):
  prompt=post('/apply-template',item)['prompt']
  return len(post('/tokenize',dict(content=prompt,parse_special=True,add_special=False))['tokens'])
 delivered,receipt=fit_tool_history(chat,count,32768)
 receipt['chat_sha256']=digest(json.dumps(delivered,sort_keys=True,ensure_ascii=False,separators=(',',':')))
 return delivered,receipt

def dump(p,d):
 p.write_text(json.dumps(d,ensure_ascii=False))
def text_content(value):
 if isinstance(value,str):return value
 if not isinstance(value,list):raise ValueError('Unsupported content representation')
 if any(x.get('type') not in ('input_text','output_text','text') for x in value):
  raise ValueError('Unsupported non-text input')
 return '\n'.join(x['text'] for x in value)
def to_chat(req,model,seed):
 tools=[]
 def add(tool,ns=''):
  if tool['type']=='namespace':
   for child in tool['tools']:add(child,tool['name']+'__')
  elif tool['type']=='function':
   tools.append({'type':'function','function':{'name':ns+tool['name'],'description':tool.get('description',''),'parameters':tool['parameters']}})
  else: raise ValueError('Unsupported tool type '+tool['type'])
 for tool in req.get('tools',[]):add(tool)
 messages=[]
 if req.get('instructions'):messages.append({'role':'system','content':req['instructions']})
 for m in req['input']:
  k=m.get('type','message')
  if k=='message':
   role=m['role'];messages.append({'role':'system' if role=='developer' else role,'content':text_content(m['content'])})
  elif k=='function_call':
   name=(m.get('namespace','')+'__' if m.get('namespace') else '')+m['name']
   tc={'type':'function','id':m['call_id'],'function':{'name':name,'arguments':m['arguments']}}
   if messages and messages[-1]['role']=='assistant':messages[-1].setdefault('tool_calls',[]).append(tc)
   else:messages.append({'role':'assistant','content':'','tool_calls':[tc]})
  elif k=='function_call_output':
   messages.append({'role':'tool','tool_call_id':m['call_id'],'content':text_content(m['output'])})
  else:raise ValueError('Unsupported history type '+k)
 # The Qwen template has a single system prefix. Keep every instruction verbatim.
 systems=[m['content'] for m in messages if m['role']=='system']
 messages=[{'role':'system','content':'\n\n'.join(systems)}]+[m for m in messages if m['role']!='system']
 return dict(model=model,messages=messages,tools=tools,stream=False,cache_prompt=True,
             seed=seed,temperature=0.7,top_p=0.8,top_k=20,max_tokens=4096,
             chat_template_kwargs={'enable_thinking':False})
def stream_result(model,data):
 uuidstr=lambda:uuid.uuid4().hex
 choice,=data['choices'];msg=choice['message']
 if choice['finish_reason']=='length': raise ValueError('Truncated local completion')
 usage=data['usage']; inp=usage['prompt_tokens'];out=usage['completion_tokens']
 assert usage['total_tokens']==inp+out
 u=dict(input_tokens=inp,output_tokens=out,total_tokens=inp+out,
        input_tokens_details={'cached_tokens':usage.get('prompt_tokens_details',{}).get('cached_tokens',0)},
        output_tokens_details={'reasoning_tokens':0})
 rid='resp_'+uuidstr();seq=[];items=[]
 def event(kind,**d):
  block=dict(type=kind,sequence_number=len(seq),**d)
  seq.append('event: '+kind+'\ndata: '+json.dumps(block,ensure_ascii=False)+'\n\n')
 def response(status):return dict(id=rid,object='response',created_at=int(time.time()),status=status,model=model,output=list(items),usage=u if status=='completed' else None)
 event('response.created',response=response('in_progress'))
 if msg.get('reasoning_content'):raise ValueError('Unexpected reasoning with thinking disabled')
 content=msg.get('content') or ''
 if content:
  i=len(items);part=dict(type='output_text',text=content,annotations=[])
  item=dict(id='msg_'+uuidstr(),type='message',role='assistant',content=[part],status='completed')
  event('response.output_item.added',output_index=i,item=dict(item,content=[],status='in_progress'))
  event('response.content_part.added',output_index=i,item_id=item['id'],content_index=0,part=dict(part,text=''))
  event('response.output_text.delta',output_index=i,item_id=item['id'],content_index=0,delta=content)
  event('response.output_text.done',output_index=i,item_id=item['id'],content_index=0,text=content)
  event('response.content_part.done',output_index=i,item_id=item['id'],content_index=0,part=part)
  event('response.output_item.done',output_index=i,item=item);items.append(item)
 for tc in msg.get('tool_calls') or []:
  fn=tc['function'];a=fn['arguments'];name=fn['name'];i=len(items)
  item=dict(type='function_call',id='fc_'+uuidstr(),call_id=tc.get('id') or 'call_'+uuidstr(),name=name,arguments=a,status='completed')
  if '__' in name:item['namespace'],item['name']=name.split('__',1)
  event('response.output_item.added',output_index=i,item=dict(item,arguments='',status='in_progress'))
  event('response.function_call_arguments.delta',output_index=i,item_id=item['id'],delta=a)
  event('response.function_call_arguments.done',output_index=i,item_id=item['id'],arguments=a)
  event('response.output_item.done',output_index=i,item=item);items.append(item)
 if not items:raise ValueError('Empty local message')
 event('response.completed',response=response('completed'))
 return ''.join(seq).encode()
class Local(BaseHTTPRequestHandler):
 def log_message(self,*_):pass
 def send(self,status,body,ct):
  self.send_response(status);self.send_header('Content-Type',ct);self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body)
 def do_POST(self):
  s=self.server
  with s.lock:s.calls+=1;n=s.calls
  try:
   assert self.path=='/v1/responses'
   req=json.loads(self.rfile.read(int(self.headers['Content-Length'])))
   dump(s.out/f'request-{n}.json',req)
   model=os.environ['PILOT_MODEL'];assert req['model']==model
   data=to_chat(req,model,3411+n)
   policy_blocks=[x.get('text','') for m in req['input'] if m.get('role')=='developer' for x in m.get('content',[]) if isinstance(x,dict)]
   if not any('<permissions instructions>' in b and 'Approval policy is currently never' in b for b in policy_blocks):
    raise ValueError('Expected never-approve benchmark policy')
   data['tools']=local_tools(data['tools'],approval_policy='never')
   used=sum(json.loads(p.read_bytes())['usage']['completion_tokens'] for p in s.out.glob('local-*.json'))
   limit=output_allowance(used,16384,8192)
   if not limit:raise ValueError('Cumulative output budget exhausted')
   data['max_tokens']=limit
   dump(s.out/f'budget-{n}.json',dict(used=used,limit=limit,total=16384))
   sess=requests.Session();sess.trust_env=False
   sess.cert=(str(ROOT/'client/client.crt'),str(ROOT/'client/client.key'))
   sess.verify=str(ROOT/'client/server.crt')
   sess.headers['Authorization']='Bearer '+(ROOT/'client/api.key').read_text().strip()
   endpoint=os.environ['PILOT_URL']
   data,context=prepare_chat(sess,endpoint,data)
   dump(s.out/f'context-{n}.json',context)
   r=sess.post(endpoint+'/v1/chat/completions',json=data,timeout=(8,3550))
   reply=r.json();dump(s.out/f'local-{n}.json',reply)
   r.raise_for_status()
   assert 0 < reply['usage']['completion_tokens'] <= limit
   body=stream_result(model,reply)
   (s.out/f'response-{n}.body').write_bytes(body)
   dump(s.out/f'response-{n}.json',dict(status=200,type='text/event-stream',route=self.path))
   self.send(200,body,'text/event-stream')
  except Exception as exc:
   with (s.out/'errors.log').open('a') as f:f.write(str(n)+' '+str(exc)[:350]+'\n')
   self.send(400,b'{"error":{"message":"local inference failed"}}','application/json')
