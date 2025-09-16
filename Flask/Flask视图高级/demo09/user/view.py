# from flask import Blueprint
#
# # 创建蓝图
# user_bp = Blueprint('user',__name__)
#from Flask视图高级.demo09.user import user_bp

from user import user_bp

# 管理的子功能
@user_bp.route('/login/')
def login():
    return '登录模块'
@user_bp.route('/register/')
def register():
    return '注册模块'