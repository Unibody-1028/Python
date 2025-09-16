from imaplib import Debug

from flask import Flask

app = Flask(__name__)

# @app.route('/article/1')
# def index1():
#     return '/article/1'
#
# @app.route('/article/2')
# def index2():
#     return '/article/2'
@app.route('/article/<id>')

def index(id):
    print(f'接收到的文章ID是：{id}')
    # 获取到ID后去数据库查询数据

    return f'返回了，{id}的文章'


if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0',port=8000)