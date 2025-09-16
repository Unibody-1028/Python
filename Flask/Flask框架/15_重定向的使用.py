from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/user_login/')
def login():
    return '登录界面'

@app.route('/info/')
def info():
    print('个人信息')
    return redirect(url_for('login')) # 重定向与url_for配合使用



if __name__ == '__main__':
    app.run(debug=True)

