# views.py: 路由 + 视图函数
from flask import Blueprint, render_template
from ..models.models import *

# 蓝图
blog = Blueprint('blog', __name__)


@blog.route('/')
@blog.route('/index/')
def blog_index():
    photos = PhotoModel.query.limit(6)
    categorys = CategoryModel.query.all()
    articles = ArticleModel.query.all()
    commends = articles[:4]
    # 返回给浏览器博客首页
    return render_template('home/index.html',
                           photos=photos,
                           categorys=categorys,
                           articles=articles,
                           commends=commends)


# 博客-我的相册
@blog.route('/photos/')
def blog_photos():
    photos = PhotoModel.query.all()
    return render_template('home/photos.html', photos=photos)


# 博客-我的日记
@blog.route('/article/')
def blog_article():
    categorys = CategoryModel.query.all()
    articles = ArticleModel.query.all()
    return render_template('home/article.html',
                           categorys=categorys,
                           articles=articles)


# 博客-关于我
@blog.route('/about/')
def blog_about():
    photos = PhotoModel.query.limit(6)
    categorys = CategoryModel.query.all()
    return render_template('home/about.html',
                           photos=photos,
                           categorys=categorys)