from flask import Flask

app = Flask(__name__)

@app.route('/string/<id>')
def index_string(id):
    print(f'接收到的文章ID是：{id}')
    # 获取到ID后去数据库查询数据
    print(type(id))

    return f'返回了，{id}的文章'

@app.route('/int/<int:id>')
def index_int(id):
    print(f'接收到的文章ID是：{id}')
    # 获取到ID后去数据库查询数据
    print(type(id))

    return f'返回了，int类型{id}的文章'
@app.route('/float/<float:id>')
def index_float(id):
    print(f'接收到的文章ID是：{id}')
    # 获取到ID后去数据库查询数据
    print(type(id))
    return f'返回了，float类型{id}的文章'

@app.route('/path/<path:id>')
def index_path(id):
    print(f'接收到的文章ID是：{id}')
    # 获取到ID后去数据库查询数据
    print(type(id))
    return f'返回了，path类型{id}的文章'

@app.route('/uuid/<uuid:id>')
def index_uuid(id):
    print(f'接收到的文章ID是：{id}')
    # 获取到ID后去数据库查询数据
    print(type(id))
    return f'返回了，uuid类型{id}的文章'

@app.route('/<any(user,item):tmp>/<int:id>')
def index_any(tmp,id):
    if tmp == 'user':
        return f"返回了一个编号为{id}的用户信息"
    elif tmp == 'item':
        return f"返回了一个编号为{id}的元素信息"

from werkzeug.routing import BaseConverter

if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0',port=8000)