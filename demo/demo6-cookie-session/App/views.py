# views.py: 路由 + 视图函数
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, session
from .models import *

# 蓝图
blue = Blueprint('user', __name__)


# 首页
@blue.route('/')
@blue.route('/home/')
def index():
    # 4. 获取 cookie
    # username = request.cookies.get('user')
    username = session.get('user')
    return render_template('home.html', username=username)


# 登录
@blue.route('/login/', methods=['GET', 'POST'])
def login():
    # GET： 访问登录页面
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        pass
        # 1. 获取前端提交过来的数据
        username = request.form.get('username')
        password = request.form.get('password')

        # 2. 模拟登录: 用户名和密码验证
        if username == 'mys' and password == '123':
            # 登录成功
            response = redirect('/home/')

        # 3. 设置cookie
        # cookie 中不能有中文
        #   response.set_cookie('user', 'mys',)  # 默认浏览器关闭则cookie失效
        # 过期时间
        #   max_age: 秒
        #   expires: 指定的 datetime 日期
        #     response.set_cookie('user', 'mys', max_age=3600*24*7)
        #     response.set_cookie('user', 'mys', expires=datetime(2024, 12, 1))

            # 设置session
            session['user'] = username
            session.permanent = True
            return response
        else:
            print('密码输入错误, 请重试')
            return '400 密码输入错误, 请重试'


# 注销
@blue.route('/logout/')
def logout():
    response = redirect('/home')
    # 5.删除cookie
    # response.delete_cookie('user')
    session.pop('user')
    return response

