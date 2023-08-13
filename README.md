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
        
        #返回值即为机器人回复文本
        #args为传入的参数，例如:用户输入为 /echo hello world ， 则参数列表为["hello","world"] ， 则echo指令返回值为 hello
        return args[0]
    
```
7. 您还可以获取通话的上下文，例如:
```python
...
@handle_event
def handle(self):
    print(self.context)
...
```
8. 更多功能正在开发中...
-----------
### 适配器编写
文档正在编写中...


