import json
from flask import Flask
app = Flask(__name__)     #创建一个wsgi应用

@app.route('/')           #添加路由：根
def hello_world():
    return 'Hello World!' #输出一个字符串


@app.route('/hello')           #添加路由：hello
def do_hello():
    return '<h1>Hello, stranger!</h1>'    #输出一个字符串

import json
...
@app.route('/json')
def do_json():
    hello = {"name":"stranger", "say":"hello"}
    return json.dumps(hello)
'''
#修改HTTP状态码
@app.route('/status_1973')
def status_1973():
    return "hello",1973
'''
#HTTP头
from flask import make_response
...
@app.route('/保密文件')
def 保密文件():
    resp = make_response('<h1>This document has a modified header!</h1>')
    resp.headers['X-Something'] = 'A value'
    resp.headers['Server'] = 'My special http server'
    return resp

#设置COokie:
from flask import make_response
...
@app.route('/set_cookie')
def set_cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('username', 'evancss')
    return response

#重定向：让浏览器打开另一个Url:
from flask import redirect
...
@app.route('/redir')
def redir():
    return redirect('http://www.baidu.com')

#使用Abort
from flask import abort
...
@app.route('/user/<id>')
def get_user(id):
    if int(id)>10:
        abort(404)
    return '<h1>Hello, %s</h1>' % id



if __name__ == '__main__':
    app.run(debug=True)             #启动app的调试模式

