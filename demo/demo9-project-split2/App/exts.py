# exts.py: 插件管理
# 扩展的第三方插件

# 1. 导入第三方插件
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 2. 初始化
db = SQLAlchemy()
migrate = Migrate()


# 3. 和 app 对象绑定
def init_exts(app):
    db.init_app(app=app)
    migrate.__init__(app=app, db=db)
