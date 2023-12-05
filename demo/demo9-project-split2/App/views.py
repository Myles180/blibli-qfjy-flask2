# views.py: 路由 + 视图函数
from flask import Blueprint
from .models import *

# 蓝图
blue = Blueprint('user', __name__)


@blue.route('/')
def index():
    # 返回给浏览器的字符串
    return 'index'
