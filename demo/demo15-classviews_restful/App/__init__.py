from flask import Flask
from .exts import init_exts
from .urls import *


def create_app():
    app = Flask(__name__)

    # 配置数据库
    db_uri = 'sqlite:///sqlite3.db'  # sqlite配置
    # db_uri = 'mysql+pymysql://root:123@localhost:3306/flaskdb'  # mysql的配置
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁止对象追踪修改

    # 初始化插件
    init_exts(app=app)

    return app

