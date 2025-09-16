from flask import Flask,session

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

# 设置Session的盐
app.config.secret_key = 'finalfancty'

# 通过类设置
class DefaultConfig:
    SECRET_KEY = 'finalfancty'

app.config.from_object(DefaultConfig)

@app.route('/set_session/')
def set_session():
    session['uname'] = 'bob'
    session['pwd'] = '123'
    return '设置了一个Session对象'

@app.route('/get_session/')
def get_session():
    uname = session.get('uname')
    pwd = session.get('pwd')
    return f'从Session读取出的数据为:{uname}---{pwd}'

@app.route('/del_session/')
def del_session():
    # pop删除一个key
    #session.pop('uname')
    # clear清空所有的key
    session.clear()
    return '删除session中的uname信息'


if __name__ == '__main__':

    app.run(debug=True,port=8088)
