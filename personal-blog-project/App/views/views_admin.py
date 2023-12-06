# views.py: 路由 + 视图函数
from flask import Blueprint, render_template, request, redirect, jsonify
from ..models.models_admin import *
from ..models.models import *
import time

# 蓝图
admin = Blueprint('admin', __name__)


# -------------------------------------- 后台管理 -------------------------------------- #
from functools import wraps


# 装饰器: 登录验证
def login_required(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        # 判断用户是否登录了
        # 获取cookie，得到登录的用户
        user_id = request.cookies.get('user_id', None)
        if user_id:
            # 登录过，进入后台管理系统
            user = AdminUserModel.query.get(user_id)
            request.user = user

            return fn(*args, **kwargs)
        else:
            # 如果没有登录，则跳转到登录页面
            return redirect('/admin/login/')

    return inner


# 后台管理-首页
@admin.route('/admin/')
@admin.route('/admin/index/')
@login_required
def index():
    # # 获取 cookie, 得到登录的用户
    # user_id = request.cookies.get('user_id', None)
    # if user_id:
    #     # 如果登陆过，进入后台管理系统
    #     user = AdminUserModel.query.get(user_id)
        user = request.user
        categorys = CategoryModel.query.filter()
        articles = ArticleModel.query.filter()
        photos = PhotoModel.query.filter()

        return render_template('admin/index.html',
                               username=user.name,
                               categorys=categorys,
                               articles=articles,
                               photos=photos
                               )
    # else:
    #     # 如果没有登录，则跳转到登录页面
    #     return redirect('/admin/login/')


# 后台管理-登录
@admin.route('/admin/login/', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'GET':
        return render_template('admin/login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        userpwd = request.form.get('userpwd')

        # 登录验证: 验证用户名和密码是否匹配
        user = AdminUserModel.query.filter_by(name=username, password=userpwd).first()
        if user:
            # 登录成功
            response = redirect('/admin/index/')
            response.set_cookie('user_id', str(user.id), max_age=7*24*3600)
            return response
        else:
            return 'Login Failed'


# 后台管理-退出登录
@admin.route('/admin/logout/')
def admin_logout():
    response = redirect('/admin/login/')
    response.delete_cookie('user_id')
    return response


# -------------------------------------- 分类管理 -------------------------------------- #
# 后台管理-分类管理
@admin.route('/admin/category/')
@login_required
def admin_category():
    user = request.user
    categorys = CategoryModel.query.all()
    return render_template('admin/category.html',
                           username=user.name,
                           categorys=categorys)


# 后台管理-添加分类
@admin.route('/admin/addcategory/', methods=['GET', 'POST'])
@login_required
def admin_addcategory():
    if request.method == 'POST':
        name = request.form.get('name')
        describe = request.form.get('describe')

        # 添加分类
        category = CategoryModel()
        category.name = name
        category.describe = describe

        try:
            db.session.add(category)
            db.session.commit()
        except Exception as e:
            print('e', e)
            db.session.rollback()

        return redirect('/admin/category/')

    else:
        return '请求方式错误！'


# 后台管理-删除分类
@admin.route('/admin/delcategory/', methods=['GET', 'POST'])
@login_required
def admin_delcategory():
    if request.method == 'POST':
        id = request.form.get('id')
        category = CategoryModel.query.get(id)

        # 删除分类
        try:
            db.session.delete(category)
            db.session.commit()
        except Exception as e:
            print('e:', e)
        return jsonify({'code': 200, 'msg': '删除成功！'})

    else:
        return jsonify({'code': 400, 'msg': '请求方式错误！'})


# 后台管理-修改分类
@admin.route('/admin/updatecategory/<id>/', methods=['GET', 'POST'])
@login_required
def admin_updatecategory(id):
    user = request.user
    category = CategoryModel.query.get(id)
    if request.method == 'GET':
        return render_template('admin/category_update.html',
                               username=user.name,
                               category=category)
    elif request.method == 'POST':
        name = request.form.get('name')
        describe = request.form.get('describe')

        # 修改
        category.name = name
        category.describe = describe

        try:
            db.session.commit()
        except Exception as e:
            print('e: ', e)

        return redirect('/admin/category/')

    else:
        return '请求方式错误'


# -------------------------------------- 文章分类 -------------------------------------- #
# 后台管理-文章管理
@admin.route('/admin/article/', methods=['GET','POST'])
@login_required
def admin_article():
    articles = ArticleModel.query.all()
    return render_template('admin/article.html',
                           username=request.user.name,
                           articles=articles)


# 后台管理-添加文章
@admin.route('/admin/addarticle/', methods=['GET', 'POST'])
@login_required
def admin_addarticle():
    if request.method == 'GET':
        categorys = CategoryModel.query.all()
        return render_template('admin/article_add.html',
                               username=request.user.name,
                               categorys=categorys)
    elif request.method == 'POST':
        name = request.form.get('name')
        keywords = request.form.get('keywords')
        category = request.form.get('category')
        content = request.form.get('content')
        img = request.files.get('img')
        # print('img:', img)
        # print('img.filename', img.filename)

        # 图片存储路径
        img_name = f'{time.time()}-{img.filename}'
        img_url = f'/static/home/uploads/{img_name}'

        # 添加文章
        try:
            article = ArticleModel()
            article.name = name
            article.keyword = keywords
            article.content = content
            article.img = img_url   # 图片路径
            article.category_id = category

            db.session.add(article)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print('e: ', e)
        else:
            # 如果上面添加到数据库成功，那么手动将图片存入本地
            img_data = img.read()
            with open(f'App/{img_data}', 'wb') as fp:
                fp.write(img_data)
                fp.flush()

        return redirect('/admin/article/')


# 后台管理-修改文章
@admin.route('/admin/updatearticle/<id>/', methods=['GET', 'POST'])
@login_required
def admin_updatearticle(id):
    article = ArticleModel.query.get(id)

    if request.method == 'GET':
        categorys = CategoryModel.query.all()
        return render_template('admin/article_update.html',
                            username=request.user.name,
                            categorys=categorys,
                            article=article)
    elif request.method == 'POST':
        # 修改文章
        name = request.form.get('name')
        keywords = request.form.get('keywords')
        category = request.form.get('category')
        content = request.form.get('content')
        img = request.files.get('img')

        # 图片存储路径
        img_name = f'{time.time()}-{img.filename}'
        img_url = f'/static/home/uploads/{img_name}'

        # 添加文章
        try:
            article = ArticleModel()
            article.name = name
            article.keyword = keywords
            article.content = content
            article.img = img_url  # 图片路径
            article.category_id = category

            db.session.add(article)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print('e: ', e)
        else:
            # 如果上面添加到数据库成功，那么手动将图片存入本地
            img_data = img.read()
            with open(f'App/{img_data}', 'wb') as fp:
                fp.write(img_data)
                fp.flush()

        return redirect('/admin/article/')


# 后台管理-删除文章
@admin.route('/admin/delarticle/', methods=['GET', 'POST'])
@login_required
def admin_delarticle():
    if request.method == 'POST':
        id = request.form.get('id')
        article = ArticleModel.query.get(id)

        try:
            db.session.delete(article)
            db.session.commit()
        except Exception as e:
            print('e: ', e)
            return jsonify({'code': 500, 'msg': '删除失败！'})

        return jsonify({'code': 200, 'msg': '删除成功'})

    return jsonify({'code': 400, 'msg': '请求方式错误！'})