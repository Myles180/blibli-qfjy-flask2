from flask import Blueprint, request, render_template, session, g, current_app
from .models import *
from .exts import cache
import time

# 蓝图
blue = Blueprint('user', __name__)


# 使用缓存
@blue.route('/')
@cache.cached(timeout=20)  # 给视图函数加一个缓存20秒
def index():
    print('Index2')
    print('index视图函数中:', g.star)

    time.sleep(5)
    return 'index2'


# AOP: 切面编程

# 钩子:钩子函数
#   也叫中间件

# before_request: 每一次请求之前访问
@blue.before_request
def before():
    print('before_request')

    # request
    # print(request.path)
    # print(request.method)
    # print(request.remote_addr)  # 客户端ip

    # 简单的反爬
    # print(request.user_agent)  # python-requests/2.28.2
    # if "python" in request.user_agent.string:
    #     return '您正在使用Python爬虫，再见！'

    # 针对IP做反爬(简单)
    ip = request.remote_addr
    # cache.get()
    # cache.set()
    if cache.get(ip):
        # 做了拦截，不会进入视图函数
        return '小伙子，别爬了！'
    else:
        # 对每个IP设置一个缓存，1秒内不让重复访问
        cache.set(ip, 'value', timeout=1)


    # Flask内置对象
    #  request：请求对象
    #  session：会话对象
    #  g：global全局对象
    #  current_app： Flask应用对象

    g.star = '杰伦'
    print(g.star)

    print(current_app)  # <Flask 'App'>
    print(current_app.config)  # <Config {'ENV': 'production', 'DEBU...


# static和templates
@blue.route('/templates/')
def templates():
    return render_template('template.html')


