# __init__.py: 初始化文件，创建 Flask 应用

# 导入Flask
from flask import Flask
from .views import blue


def create_app():
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(blueprint=blue)

    return app
