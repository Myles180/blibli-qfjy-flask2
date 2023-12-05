# 导入Flask
from flask import Flask, render_template  # ,jsonify

# 创建Flask应用
app = Flask(__name__)


# 路由 route + 视图函数 hello_world
@app.route('/')
# put application's code here
def home():
    # 返回给浏览器的字符串
    return 'Flask home2!'


# 模版渲染
@app.route('/index/')
def index():
    # 1. 返回字符串: 支持 HTML 标签
    # return '<b>Index 首页</b>'
    # 2. 模版渲染
    return render_template('home.html', name='法外狂徒张三')
    # 3. JSON
    # jsonify: 序列化
    # return jsonify({'name': '张三', 'age': 33})


if __name__ == '__main__':
    # 启动服务器
    app.run(debug=True, port=5000, host='0.0.0.0')
