from functools import wraps
import logging
from flask import Flask, render_template,request
from flask.views import MethodView

# 设置日志模块
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        uname = request.args.get('uname')
        pwd = request.args.get('pwd')
        if uname == 'zs' and pwd == '123':
            logging.info(f"{uname}登录成功")
            return func(*args,**kwargs)
        else:
            logging.info(f"{uname}尝试登录失败")
            return "用户名或密码错误"
    return wrapper

def logger(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        logging.warning('这是日志测试信息')
        return func(*args,**kwargs)
    return wrapper

@app.route('/')
@login_required
def index():
    return 'hello'


class LoginView(MethodView):
    decorators = [login_required,logger]

    def get(self):
        return 'Hello'
app.add_url_rule('/login/',view_func=LoginView.as_view('login'))

if __name__ == '__main__':
    app.run(debug=True,port=8088)


