from flask import Flask,request,g
from signals import login_space

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/login/')
def login():
    uname = request.args.get('uname')

    if uname:
        g.name = uname
        login_space.send()
        return '登录成功'
    else:
        return '请登录'


if __name__ == '__main__':
    app.run(debug=True,port=8088)

