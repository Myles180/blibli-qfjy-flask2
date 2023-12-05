# views.py: 路由 + 视图函数
import random

from flask import Blueprint, request

from .models import *

# 蓝图
blue = Blueprint('user', __name__)


@blue.route('/')
def index():
    # 返回给浏览器的字符串
    return 'index'

# 多表操作


# ------------------------------- 一对多 --------------------------------- #
# 增加数据
@blue.route('/addbanji/')
def add_banji():
    # 添加班级
    banjis = []
    for i in range(10):
        banji = BanJi()
        banji.name = f'Jay{i}-' + str(random.randint(10, 99))
        banjis.append(banji)
    try:
        db.session.add_all(banjis)
        db.session.commit()
    except Exception as e:
        print('e: ', e)
        db.session.rollback()
        db.session.flush()

    return 'OK'


@blue.route('/addstu/')
def add_stu():
    # 添加学生
    students = []
    for i in range(10, 20):
        stu = Student()
        stu.name = f'Lucy{i}'
        stu.age = i
        stu.banji_id = random.randint(1, 2)
        students.append(stu)
    try:
        db.session.add_all(students)
        db.session.commit()
    except Exception as e:
        print('e: ', e)
        db.session.rollback()
        db.session.flush()

    return 'OK'


# 修改
@blue.route('/updatestu/')
def update_stu():
    # 添加学生
    stu = Student.query.first()
    stu.age = 100
    db.session.commit()

    return 'OK'


# 删除
@blue.route('/delstu/')
def del_stu():
    # 删除学生
    stu = Student.query.first()
    db.session.delete(stu)
    db.session.commit()

    return 'OK'


# 删除
@blue.route('/delbanji/')
def del_banji():
    # 删除班级
    banji = BanJi.query.first()
    db.session.delete(banji)
    db.session.commit()

    return 'OK'


# 查询
@blue.route('/getstu/')
def get_stu():
    # 查询某学生所在的班级: 反向引用 banji
    stu = Student.query.get(5)
    print(stu.name, stu.age)
    print(stu.banji_id, stu.banji, stu.banji.name, stu.banji.id)

    # 查询某个班级下的所有学生
    banji = BanJi.query.get(2)
    print(banji.name)
    print(banji.students)
    for stu in banji.students:
        print(stu.name, stu.age)

    return 'OK'


# ------------------------------- 多对多 --------------------------------- #
@blue.route('/adduser/')
def add_user():
    # 添加用户
    users = []
    for i in range(10, 14):
        user = UserModel()
        user.name = f'Lucy{i}'
        user.age = i
        users.append(user)
    try:
        db.session.add_all(users)
        db.session.commit()
    except Exception as e:
        print('e: ', e)
        db.session.rollback()
        db.session.flush()

    return 'OK'


@blue.route('/addmovie/')
def add_movie():
    # 添加电影
    movies = []
    for i in range(10, 14):
        movie = Movie()
        movie.name = f'阿凡达-{i}'
        movies.append(movie)
    try:
        db.session.add_all(movies)
        db.session.commit()
    except Exception as e:
        print('e: ', e)
        db.session.rollback()
        db.session.flush()

    return 'OK'


@blue.route('/addcollect/')
def add_collect():
    # 用户收藏电影
    user = UserModel.query.get(4)
    movie = Movie.query.get(4)

    user.movies.append(movie)
    db.session.commit()

    return 'OK'


# 查询
@blue.route('/getcollect/')
def get_collect():
    # 查找某用户收藏的所有电影
    user = UserModel.query.get(1)
    print(user.movies)
    print(list(user.movies))

    # 收藏了某电影的所有用户
    movie = Movie.query.get(4)
    print(movie.users)
    print(list(movie.users))

    return 'OK'


# 删除
@blue.route('/deluser/')
def del_user():
    # 级联删除
    user = UserModel.query.get(1)

    db.session.delete(user)
    db.session.commit()

    return 'OK'
