from sys import prefix

from flask import Flask,Blueprint

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

# 创建蓝图
user_bp = Blueprint('user',__name__)

# 管理的子功能
@user_bp.route('/login/')
def login():
    return '登录模块'
@user_bp.route('/register/')
def register():
    return '注册模块'


# 创建蓝图
item_bp = Blueprint('item',__name__)

# 管理的子功能
@item_bp.route('/item/')
def login():
    return '产品模块'


# 注册蓝图
app.register_blueprint(user_bp,url_prefix='/user')
app.register_blueprint(item_bp,url_prefix='/goods')


if __name__ == '__main__':
    app.run(debug=True,port=8088)


