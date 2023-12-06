# __init__.py ：初始化文件，创建Flask应用

from flask import Flask
from .views import blue
from .exts import init_exts


def create_app():
    app = Flask(__name__)
    # 注册蓝图
    app.register_blueprint(blueprint=blue)

    # 配置数据库
    # db_uri = 'sqlite:///sqlite3.db'  # sqlite配置
    db_uri = 'mysql+pymysql://root:123@localhost:3306/bookdb'  # mysql的配置
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁止对象追踪修改

    # 初始化插件（写在配置数据库之后）
    init_exts(app=app)

    return app

