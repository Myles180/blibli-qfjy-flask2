from App import create_app

app = create_app()

if __name__ == '__main__':
    # 启动服务器
    app.run(Debug=True, port=5000, host='0.0.0.0')
