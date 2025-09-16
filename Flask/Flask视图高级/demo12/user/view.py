from user import user_bp

@user_bp.route('/login/')
def index():
    return '用户主页'

