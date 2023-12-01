# views.py: 路由 + 视图函数
from flask import Blueprint
from .models import *

# 蓝图
blue = Blueprint('user', __name__)


@blue.route('/')
def index():
    # 返回给浏览器的字符串
    return 'index'

# 路由参数
#     string 接收任何没有斜杠（'/'）的字符串（默认）
#     int	接收整型
#     float	接收浮点型
#     path	接收路径，可接收斜线（'/'）
#     uuid	只接受uuid字符串，唯一码，一种生成规则
#     any	可以同时指定多种路径，进行限定


# string: 重点
@blue.route('/string/<string:username>/')
def get_string(username):
    print(username)
    print(type(username))
    return username


# int
@blue.route('/int/<int:id>/')
def get_id(id):
    print(id)
    print(type(id))
    return str(id)


# float
@blue.route('/float/<float:money>/')
def get_float(money):
    print(money)
    print(type(money))
    return str(money)


# path
@blue.route('/path/<path:name>/')
def get_path(name):
    print(name)
    print(type(name))
    return str(name)


# uuid
@blue.route('/uuid/<uuid:id>/')
def get_uuid(id):
    print(id)
    print(type(id))
    return str(id)


# 获取 /uuid/<uuid:id>/ 的uuid
# get_uuid
@blue.route('/get_uuid/')
def get_uuid2():
    import uuid
    return str(uuid.uuid4())


# 从列出的项目中选择一个
@blue.route('/any/<any(apple, orange, banana):fruit>/')
def get_any(fruit):
    print(fruit)
    print(type(fruit))
    return str(fruit)


# methods: 请求方式
#   默认不支持POST
#   如果需要同时支持GET和POST，就设置methods
@blue.route('/methods/', methods=['GET', 'POST'])
def get_methods():
    return 'methods'

