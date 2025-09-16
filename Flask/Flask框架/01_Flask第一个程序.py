# 使用Flask对象创建一个Web应用
from flask import Flask

# 创建对象
app = Flask(__name__)

# 路由的地址
@app.route('/index')
def index():
    # return代表将数据返回给浏览器
    return 'Mac'
if __name__ == '__main__':
    # 启动Web应用服务
    # 使用port修改端口号
    app.run(port=5000)


