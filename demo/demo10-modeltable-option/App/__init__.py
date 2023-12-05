# __init__.py: 初始化文件，创建 Flask 应用

# 导入Flask
from flask import Flask
from .views import blue
from .exts import init_exts


def create_app():
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(blueprint=blue)

    # 配置数据库
    # db_uri = 'sqlite:///sqlite3.db'  # sqlite 配置
    db_uri = 'mysql+pymysql://root:Ali%4012345@123.207.58.37:3306/flaskdb'  # mysql 配置
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 初始化插件
    init_exts(app=app)

    return app
