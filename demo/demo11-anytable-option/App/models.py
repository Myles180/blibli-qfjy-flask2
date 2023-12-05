# models.py: 模型数据库
from .exts import db

# 模型  --> 数据库
# 类  --> 表结构
# 类属性  --> 表字段
# 一个对象  --> 表的一行数据


# 多表关系
# -------------------------------一对多--------------------------------- #
# 班级:学生 = 1:N
# 班级表
class BanJi(db.Model):
    # 表名
    __tablename__ = 'banji'
    # 定义表字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    # 建立关联
    # 第一个参数: 关联的模型名(表)
    # 第二个参数: 反向引用的名称，grade对象，让student去反过来得到BanJi对象的名称: student.BanJi
    # 第三个参数: 懒加载
    # 这里的students不是字段，是一个类属性
    students = db.relationship('Student', backref='banji', lazy=True)


# 学生表
class Student(db.Model):
    # 表名
    __tablename__ = 'student'
    # 定义表字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    age = db.Column(db.Integer)
    # 外键
    banji_id = db.Column(db.Integer, db.ForeignKey(BanJi.id))


##
# ------------------------------- 多对多 --------------------------------- #
# 用户:电影 = N : M
# 中间表:收藏表
collect = db.Table(
    'colllects',
    db.Column('user_id', db.Integer, db.ForeignKey('usermodel.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True)
)


# 用户表
class UserModel(db.Model):
    __tablename__ = 'usermodel'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)


# 电影表
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))

    # 关联表
    users = db.relationship('UserModel', backref='movies', lazy='dynamic', secondary=collect)
