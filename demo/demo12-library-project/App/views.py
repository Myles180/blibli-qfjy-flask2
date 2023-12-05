from flask import Blueprint, request, render_template
from .models import *

# 蓝图
blue = Blueprint('book', __name__)

# 要求:
# 	1.在书籍的book_index.html中有一个"查看所有书籍"的超链接按钮，点击进入书籍列表book_list.html页面.
# 	2.在书籍的book_list.html中显示所有书名，点击书名可以进入书籍详情book_detail.html
# 	3.在书籍book_detail.html中可以点击该书的作者和出版社，
#     	进入作者详情的author_detail.html和
#     	出版社详情的publisher_detail.html页面


@blue.route('/')
@blue.route('/bookindex/')
def book_index():
    return render_template('book_index.html')


@blue.route('/booklist/')
def book_list():
    books = Book.query.all()
    return render_template('book_list.html', books=books)


@blue.route('/bookdetail/<int:bid>/')
def book_detail(bid):
    book = Book.query.get(bid)
    return render_template('book_detail.html', book=book)


# 作者详情
@blue.route('/authordetail/<int:aid>/')
def author_detail(aid):
    author = Author.query.get(aid)
    return render_template('author_detail.html', author=author)


# 出版社详情
@blue.route('/publisherdetail/<int:pid>/')
def publisher_detail(pid):
    publisher = Publisher.query.get(pid)
    return render_template('publisher_detail.html', publisher=publisher)

