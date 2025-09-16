from flask import Flask, session
from datetime import timedelta
app = Flask(__name__)
# 设置盐
app.secret_key = 'finalfancty'
# 修改Flask默认的31天session为2天
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=2)

@app.route('/')
def index():
    return 'Hello'

@app.route('/set_session/')
def set_session():
    # session持久化
    # 默认是31天
    session.permanent = True
    session['uname'] = 'bob'
    return '设置了一个Session信息'


@app.route('/get_session/')
# 如果服务器中途关闭,session的有效期仍然生效
# 如果盐(secrte_key)设置为固定值,那么服务器重启不会影响session的有效期
# 如果盐(secrte_key)设置随机值,服务器重启后session全部失效

def get_session():
    return session.get('uname')

if __name__ == '__main__':
    app.run(debug=True,port=8088)


