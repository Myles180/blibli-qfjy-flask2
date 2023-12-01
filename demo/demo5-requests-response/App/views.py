# views.py: 路由 + 视图函数

from flask import Blueprint, request, render_template, \
    jsonify, make_response, Response, redirect, url_for, abort
from .models import *

# 蓝图
blue = Blueprint('user', __name__)


@blue.route('/')
def index():
    return 'index'


# 请求和响应
#  request: 请求
#  response: 响应

# http一次前后端交互：先请求，后响应

# Request: 客户端向服务器发送的请求
@blue.route('/request/', methods=['GET', 'POST'])
def get_request():
    pass
    # print(request)  # <Request 'http://127.0.0.1:5000/request/' [GET]>

    # 重要属性
    print(request.method)  # 请求方式，'GET'或'POST'...
    # GET请求的参数
    #  ImmutableMultiDict: 类字典对象，区别是可以出现重复的key
    print(request.args)  # ImmutableMultiDict([('name', 'lisi'), ('name', 'wangwu'), ('age', '33')])
    # print(request.args['name'], request.args['age'])  # lisi 33
    # print(request.args.get('name'))  # lisi
    # print(request.args.getlist('name'))  # ['lisi', 'wangwu']

    # POST请求的参数
    print(request.form)  # ImmutableMultiDict([('name', 'lucy'), ('age', '33')])
    # print(request.form.get('name'))  # lucy

    # cookie
    print(request.cookies)  # ImmutableMultiDict([('name', 'hello')])

    # 路径
    print(request.path)  # /request/
    print(request.url)   # http://127.0.0.1:5000/request/?name=lisi&name=wangwu&age=33
    print(request.base_url)  # http://127.0.0.1:5000/request/
    print(request.host_url)  # http://127.0.0.1:5000/
    print(request.remote_addr)  # 127.0.0.1，客户端的ip

    print(request.files)  # 文件内容 ，ImmutableMultiDict([])
    print(request.headers)  # 请求头
    print(request.user_agent)  # 用户代理，包括浏览器和操作系统的信息 ， python-requests/2.28.2

    return 'request ok!'


# Response: 服务器端向客户端发送的响应
@blue.route('/response/')
def get_response():
    pass
    # 响应的几种方式
    # 1. 返回字符串（不常用）
    # return 'response OK!'

    # 2. 模板渲染 (前后端不分离)
    # return render_template('index.html', name='张三', age=33)

    # 3. 返回json数据 (前后端分离)
    data = {'name': '李四', 'age': 44}
    # return data

    # jsonify(): 序列化，字典=>字符串
    # return jsonify(data)

    # 4. 自定义Response对象
    html = render_template('index.html', name='张三', age=33)
    print(html, type(html))  # <class 'str'>

    # res = make_response(html, 200)
    res = Response(html)
    return res


# Redirect: 重定向
@blue.route('/redirect/')
def make_redirect():
    pass
    # 重定向的几种方式
    # return redirect('https://www.qq.com')
    # return redirect('/response/')

    # url_for():反向解析,通过视图函数名反过来找到路由
    #    url_for('蓝图名称.视图函数名')
    # ret = url_for('user.get_response')
    # print('ret:', ret)  # /response/
    # return redirect(ret)

    # url_for传参
    ret2 = url_for('user.get_request', name='王五', age=66)
    return redirect(ret2)


# 异常处理
# 抛出异常：abort
@blue.route('/abort/')
def make_abort():
    # 主动抛出异常
    abort(500)
    return 'hello abort'


# 捕获异常
@blue.errorhandler(500)
def error_handler(e):
    print('e:', e)
    return '捕获到异常:' + str(e)





