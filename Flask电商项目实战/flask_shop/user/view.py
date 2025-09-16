from flask_shop.user import user # 导入蓝图

@user.route('/login')
def login():
    return 'User login page'

@user.route('/')
def index():
    return 'User index page'