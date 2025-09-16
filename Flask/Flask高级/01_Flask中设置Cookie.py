from flask import Flask,make_response,request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello"
# 设置Cookie
@app.route('/set_cookie/')
def set_cookie():
    resp = make_response('设置了一个cookie信息')
    resp.set_cookie('uname','jack')
    return resp
# 获取Cookie
@app.route('/get_cookie/')
def get_cookie():
    uname = request.cookies.get('uname')
    return f'Cookie里面的内容是:{uname}'
# 删除Cookie

@app.route('/del_cookie/')
def del_cookie():
    resp = make_response('删除cookie')
    resp.delete_cookie('uname')
    return resp


if __name__ == '__main__':
    app.run(debug=True,port=8088)


