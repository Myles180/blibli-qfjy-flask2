# __init__.py: 初始化文件，创建 Flask 应用
import datetime

# 导入Flask
from flask import Flask
from .views import blue


def create_app():
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(blueprint=blue)
    # session 配置
    print(app.config)  # flask 配置信息
    app.config['SECRET_KEY'] = 'abc123'
    # 设置 session 过期时间
    app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=8)
    return app
