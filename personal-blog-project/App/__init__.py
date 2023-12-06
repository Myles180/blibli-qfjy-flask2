# __init__.py: 初始化文件，创建 Flask 应用

# 导入Flask
from flask import Flask
from .views.views import blog
from .views.views_admin import admin
from .exts import init_exts


def create_app():
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(blueprint=blog)  # 博客前端页面
    app.register_blueprint(blueprint=admin)  # 博客后台管理系统

    # 配置数据库
    db_uri = 'mysql+pymysql://root:123@localhost:3306/blogdb'  # mysql 配置
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 初始化插件
    init_exts(app=app)

    return app
