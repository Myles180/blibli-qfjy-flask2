# models.py: 模型数据库
from ..exts import db

# 模型  --> 数据库
# 类  --> 表结构
# 类属性  --> 表字段
# 一个对象  --> 表的一行数据


# 必须继承 db.Model
class AdminUserModel(db.Model):
    # 表名
    __tablename__ = 'tb_adminuser'
    # 定义表字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))


