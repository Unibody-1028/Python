from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route('/test/')
def test_url():
    # 如果想要返回蓝图中的url地址,需要在函数名前加上蓝图的名称
    return url_for('user.index')



@app.route('/test_tmp/')
def test_static():
    return render_template('index.html')

from user import user_bp
app.register_blueprint(user_bp,url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True,port=8088)


