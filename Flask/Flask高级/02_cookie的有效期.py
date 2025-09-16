from flask import Flask,Response

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/create_cookie/default/')
def create_cookie1():
    resp = Response('通过默认值设置cookie有效期')
    # 没有设置有效期时,cookie会在浏览器关闭时过期
    resp.set_cookie('uname','bob')
    return resp
@app.route('/create_cookie/max_age')
def create_cookie2():
    resp = Response('通过max_age设置cookie有效期')
    # 设置有效期为2小时
    age = 2*60*60
    resp.set_cookie('uname','bob',max_age=age)
    return resp

from datetime import datetime,timedelta

@app.route('/create_cookie/expires')
def create_cookie3():
    resp = Response('通过expires设置cookie有效期')
    # 设置某个时间为有效期
    tmp_time = datetime(2025,10,1,00,00,00)
    resp.set_cookie('uname','bob',expires=tmp_time)
    return resp

@app.route('/create_cookie/expires2')
def create_cookie4():
    resp = Response('通过expires设置cookie有效期')
    # 设置某个时间为有效期
    # datetime.now()得到的是英国格林尼治时间
    tmp_time = datetime.now()+timedelta(days=2)
    resp.set_cookie('uname','bob',expires=tmp_time)
    return resp

if __name__ == '__main__':
    app.run(debug=True,port=8088)

