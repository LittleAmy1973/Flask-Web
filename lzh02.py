# -*- coding: utf-8 -*-：
#继承
import json,pprint,sys
from flask import Flask, render_template
app = Flask(__name__)  #此处代表模板自动生成了一个地方
# ...

'''
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

#和  列表   有关的
@app.route('/hello')
def hello():
    users = [{"username":"users1","url":"/users/user1"},
             {"username":"users2","url":"/users/user2"}]
    return render_template("hello.html",title="User List",users=users)

'''
#继承：子类
@app.route('/child')
def child1():
    return render_template("child.html")

# 增加一个  路由 strings
@app.route('/strings')
def strings():
    return render_template("strings.html",user="ivan wang",
                            myhtmlstr="<strong>this is <i>emphasized</i></strong>")
#增加一个路由 numerics
@app.route('/numerics')
def numerics():
    return render_template("numerics.html",n1=3.14159,n2=29838721)


if __name__ == '__main__':
    app.run(debug=True)


