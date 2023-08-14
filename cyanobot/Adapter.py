import json
from typing import List
from .Logger import log
from .Bot import Bot

from http.server import HTTPServer, BaseHTTPRequestHandler

class Adapter():
	def __init__(self,bots: List[Bot]):
		#初始化适配器
		log('INFO','适配器初始化中')
		self.host = ('127.0.0.1',8080)
		
		self.Resquest.bots=bots
		
		#开始监听
		server = HTTPServer(self.host,self.Resquest)
		log('SUCCESS','适配器已就绪,开始监听'+self.host[0]+':'+str(self.host[1]))
		server.serve_forever()
		
	def handle_event(self,event):
		...
 
	class Resquest(BaseHTTPRequestHandler):
		timeout = 10
		server_version = "Apache"
		bots=[]
		def __init__(self,request,client_address,server):
			super().__init__(request,client_address,server)
			
		def check_event(self,event):
		#检查数据合法性
			if 'event_id' not in event:
				log('ERROR','Invalid event:Missing event_id')
				return False
			
			elif 'data' not in event or not event['data']:
				log('ERROR','Invalid event:Missing data')
				return False
			
			elif 'self' not in event or not event['self'] or not event['self']['bot_id']:
				log('ERROR','Invalid event:Missing self information')
				return False
				
			
			
			else:
				#检查bot是否存在
				ifexist=False
				for bot in Adapter.Resquest.bots:
					if bot.bot_id==event['self']['bot_id']:
						
						ifexist=True
						
				if ifexist:
					#以上检查均通过，则进入时间处理
					log('SUCCESS','事件合法')
					return True
				else:
					log('ERROR','request bot not found')
					return False
		
		def do_GET(self):
			self.send_response(401)
			#设置响应头
			self.send_header("Content-type","text/html")
			self.end_headers()
			buf = 'method error , please use "POST" to connect with this host'
			self.wfile.write(buf.encode())
 
		def do_POST(self):
			path = self.path
			log('INFO','接收到对'+self.path+'的请求')
       	 #获取post提交的数据
			datas = self.rfile.read(int(self.headers['content-length']))
        	
			try:
				 event = json.loads(datas)
			except Exception as e:
			 	log('ERROR','数据格式非json')
			 	log('ERROR',str(e))
			 	self.send_response(403)
			 	self.send_header("Content-type","text/html")  
			 	self.end_headers()
			 	buf = 'invalid json data'
			 	self.wfile.write(buf.encode())
			 	
			 	return False
			 	
        	
			if not datas or not self.check_event(event):
				self.send_response(403)
				self.send_header("Content-type","text/html")  
			
				self.end_headers()
				buf='invalid request event'
 
			
				self.wfile.write(buf.encode())
			
			else:
				log('SUCCESS','成功接收事件')
				self.send_response(200)
				self.send_header("Content-type","application/json")  
			
				self.end_headers()
				
				#连接到指定bot
				for bot in Adapter.Resquest.bots:
					if bot.bot_id==event['self']['bot_id']:
						buf=bot.handle(event)
				
				if buf!='blank response':
					log('INFO','机器人回复'+buf['bot_data']['message'])
					self.wfile.write(buf['bot_data']['message'].encode())
				else:
					log('INFO','机器人回复'+buf)
					
					self.wfile.write(buf.encode())
			
if __name__=='__main__':
	payload={
		'event_id':'123456789',
		'data':{
			'message':'hello'
		},
		'self':{
			'user_id':'123456789'
		},
	}
	#adapter = Adapter()
			
		
			
		
