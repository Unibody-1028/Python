from flask import Flask,url_for

app = Flask(__name__)

@app.route('/index')
def index():
    return f"Hello"

@app.route('/home/<int:uid>')
def home(uid):
    return f'this is home page{uid}'



@app.route('/show_url')
def show_url():
    #url = url_for('home') # 第一个参数是函数的名字

    url = url_for('home',uid=1001) # 根据函数名和指定的参数查找URL

    url = url_for('home', uid=1001,addr='beijing')  # 匹配不上就会以查询参数进行传递

    return f'反向查找到的URL地址是{url}'


if __name__ == '__main__':
    app.run(debug=True)


