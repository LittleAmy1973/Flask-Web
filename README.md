# Flask-Web
flask框架学习
1.1使用虚拟环境
虚拟环境：
python 解释器的一个私有副本；
不影响 全局python解释器；
为每个程序单独创建虚拟环境；
不用管理员权限。
创建虚拟环境：
工具：Virtualenv（安装方式详见《》）
激活虚拟环境：
$ venv\Scripts\activate（激活命令）
(venv) $		（激活后显示）
Ps: 输入deactivate返回
如图：



1.2使用pip安装 Python包
验证Flask是否安装正确的操作：



2.1 初始化
创建程序实例：
from flask import Flask
app = Flask(__name__)

2.2 路由和视图函数
路由：处理URL 和 函数 之间关系的程序
使用 app.route修饰器声明路由：
@app.route('/')
def index():
return '<h1>Hello World!</h1>'

2.3 启动服务器
使用 run 方法启动 Flask 集成的开发 Web 服务器：
if __name__ == '__main__':
app.run(debug=True)


2.4 一个完整的程序
Hello.py(一个完整的flask程序)：
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
return '<h1>Hello World!</h1>'
if __name__ == '__main__':
app.run(debug=True)
截图：

若是加了动态路由，则效果截图为：






2.5.1 程序和请求上下文
Hello.py(一个完整的flask程序)：
from flask import Flask
app = Flask(__name__)


















