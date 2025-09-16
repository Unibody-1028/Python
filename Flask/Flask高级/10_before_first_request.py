from flask import Flask

# 初始化函数
def init_app(app):
    print('这是第一次请求需要执行的初始化逻辑...')

# 应用工厂
def create_app():
    app = Flask(__name__)
    # 调用初始化函数
    init_app(app)
    return app

app = create_app()

@app.route('/')
def index():
    print('hello')
    return 'Hello'



if __name__ == '__main__':
    app.run(debug=True, port=8088)