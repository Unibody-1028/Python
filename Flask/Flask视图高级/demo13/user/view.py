from user import user_bp

@user_bp.route('/login/')
def login():
    return '登录模版'
