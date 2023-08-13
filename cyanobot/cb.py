from .Adapter import Adapter
from .Bot import Bot
from .Logger import log

class cb():
	adapter: Adapter
	bots: list[Bot] =[]
	
	@classmethod
	def bots_regist(cls,bot_id):
		cls.bots.append(Bot(bot_id))
		
	@classmethod
	def plugins_regist(cls,plugin_name):
		for b in cls.bots:
			b.plugins_regist(plugin_name)
	
	@classmethod
	def run(cls):
		log('INFO','cyanobot 开始运行')
		adapter=Adapter(cls.bots)
		
		
class command():
	def __init__(self,command):
		pass
		
class define_plugin():
	def __init__(self):
		self.plugin_data={}
	def get_information(self):
		return self.plugin_data