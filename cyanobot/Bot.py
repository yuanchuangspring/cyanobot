from typing import List
from .Logger import log


class Bot():
	def __init__(self,bot_id):
		#储存上下文
		self.context=[]
		#bot 识别id
		self.bot_id=bot_id
		#注册插件
		self.plugins=[]
		
		#指令开头符号
		self.BEGINWITH='/'
		
		log('SUCCESS','bot(id:'+self.bot_id+')初始化成功')
		
	def plugins_regist(self,plugin_name):
		#注册插件
		try:
			p=__import__('plugins.'+plugin_name,fromlist=[plugin_name])
			self.plugins.append(p)
			log('SUCCESS','成功加载插件'+p.plugin_data['name'])
		except Exception as e:
			log('ERROR','加载插件'+plugin_name+'失败! 失败原因:'+str(e))
		
	def handle(self,event):
		#储存上下文
		self.context.append(event)
		
		#处理原始文本，匹配其中的指令
		args_list=[]
		argtem=''
		cdstart=False
		match_cd=''
		for s in event['data']['message']:
			if s == self.BEGINWITH:
				cdstart=True
				continue
			if cdstart:
				if s==' ':
					cdstart=False
				else:
					match_cd+=s
			else:
				if s==' ':
					if not argtem=='':
						args_list.append(argtem)
						argtem=''
				else:
					argtem+=s
					
		if not argtem=='':
			args_list.append(argtem)
					
		if not match_cd:
			
			for e in reversed(self.context):
					if 'bot_data' in e:
						if 'require' in e['bot_data']:
							cur_args=e['bot_data']['cur_args']
							cur_args[e['bot_data']['require']]=args_list[0]
							match_cd = e['bot_data']['command']
							args_list=cur_args
						break
		
		#从注册事件中寻找目标指令
		for itplu in self.plugins:
			for itcd in itplu.plugin_data['commands']:
				if itcd == match_cd:
					cdobj=itplu.plugin_data['commands'][itcd](args_list,self.context)
					result=cdobj.handle()
					self.context.append(result)
					return result
		
		return 'blank response'
		
		
		
	def run(self):
		#开启监听
		pass
		
if __name__ == '__main__':
	bot=Bot('3358851903')
