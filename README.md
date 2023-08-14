# 氰机cyanoBot👋
*即问即答，api请求式bot框架，适用于网页聊天机器人*

------------

### 我们的优势
1. 无需调用其他api，直接在web对话中返回结果
2. 适配器编写简单易上手，快速对接第三方平台
3. 储存上下文信息，对话功能更加灵活

------------

### 开始使用
#### 1. 安装
`pip install cyanobot`
#### 2. 引入
`from cyanobot.cb import *`
#### 3. 注册机器人
`cb.bots_regist( bot_id  )`
注:bot_id为机器人识别码，必填，该方法请在运行前调用
#### 4. 运行
`cb.run()`

------------
### 插件
#### 1. 注册插件
```python
#注册插件，请在cb.run()前执行
cb.pugins_regist(插件名称)
```
#### 2. 编写插件
1. 在根目录下创建plugins文件夹
2. 在plugins下创建与插件名同名的文件夹
3. 在插件名文件夹中创建文件__init__.py
4. 现在，如果您想创建一个名为echo的插件，您的目录应该如下所示:
```
┣ main.py   #项目主文件
┗ plugins/
  ┗ echo/
    ┗ __init__.py
```
5. 接下来，您可以在__init.py__中编写插件详细信息，例如:
```python
#echo插件
plugin_data={
    'name':'echo',  #插件名
    'version':'1.0', #插件版本
	'description':'echo', #介绍
    'commands':{ #注册指令
        'echo':echo	#键名为指令名，键值为指令对象
    }
}
```
6. 然后，您应该创建指令对象(请确保该指令已经在plugin_data中注册)，例如:
```python
class echo(on_command): #继承指令类
    @handle_event
    def handle(self):#必填函数
        #args为传入的参数，例如:用户输入为 /echo hello world ， 则参数列表为["hello","world"] ， 则echo指令返回值为 hello
        return self.send(args[0])
    
```
7. 如果您想对各项参数进行命名，可以进行如下操作:
```python
#假设您设计了一个获取天气的指令 weather
#您希望用户输入 /weather <城市> <日期>
#参数缺少时，您希望机器人进行追问
class weather(on_command):
    #必填，声明该指令的参数名称，第一个参数将被自动命名为'城市'
    require_arg_names=['城市','日期']
    #若require arg names不为空，则返回的self.args为一个字典，键名为参数名，键值为参数值
    @handle_event
    def handle(self):
	if not self.args['城市']:
            #require函数将对信息进行标记，并发送回用户
            #require 第一个参数为返回的文本，第二个参数为请求的参数名称，第三个为当前参数列表
            return self.require('请输入城市','城市',self.args)
        elif not self.args['日期']:
            return self.require('请输入日期','日期',self.args)
        #参数齐全，返回天气信息
	return self.send(...)
```
效果如下:
```
用户输入:/weather

bot返回:请输入城市

用户输入:北京

bot返回:请输入日期

用户输入:1月11日

bot返回:...
```
8. 您还可以自行获取通话的上下文，例如:
```python
...
@handle_event
def handle(self):
    print(self.context)
...
```
9. 更多功能正在开发中...
-----------
### 适配器编写
文档正在编写中...


