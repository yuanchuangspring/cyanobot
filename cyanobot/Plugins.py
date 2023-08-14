#指令类
class on_command():
	require_arg_names=[]
	def __init__(self,args,context):
		self.args={}
		
		self.context=context
		
		#对参数进行命名
		if self.require_arg_names and not isinstance(args,dict):
			self.args['addon']=[]
			for i in range(0,len(args)):
				if i <= len(self.require_arg_names)-1:
					self.args[self.require_arg_names[i]]=args[i]
				else:
					self.args['addon'].append(args[i])
			for name in self.require_arg_names:
				if not name in self.args:
					self.args[name]=''
		else:
			self.args=args
			
				
					
	def handle(self):
		...
	def send(self,msg):
		return {'bot_data':{'message':msg}}
	def require(self,msg,arg_name,cur_args):
		return {'bot_data':{'message':msg,'command':type(self).__name__,'require':arg_name,'cur_args':cur_args}}

#事件处理逻辑
def handle_event(func):
			def handle_i(self):
				try:
					r=func(self)
					return r
				except Exception as e:
					return {'bot_data':{'error':e,'message':''}}
			return handle_i
			
			

