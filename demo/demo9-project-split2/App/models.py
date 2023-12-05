# models.py: 模型数据库
from .exts import db

# 模型  --> 数据库
# 类  --> 表结构
# 类属性  --> 表字段
# 一个对象  --> 表的一行数据


# 模型 Model: 类
# 必须继承 db.Model
class User(db.Model):
    # 表名
    __tablename__ = 'tb_user'
    # 定义表字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True, index=True)
    age = db.Column(db.Integer, default=True)

# db.Column: 表示字段
# db.Integer: 表示整数
# primary_key=True: 表示主键
# autocrement=True: 表示自动递增
# db.String(30): 表示可变字符串，等同于 varchar(30)
