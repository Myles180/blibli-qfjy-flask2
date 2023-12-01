# 导入Flask
from flask import Flask

# 创建Flask应用
app = Flask(__name__)


# 路由 route + 视图函数 hello_world
@app.route('/')
# put application's code here
def hello_world():
    # 响应：返回给浏览器的数据
    return 'Hello World!'


# 添加一个路由和视图函数
@app.route('/index/')
def index():
    return 'Index 首页'


if __name__ == '__main__':
    # 启动服务器
    app.run()
