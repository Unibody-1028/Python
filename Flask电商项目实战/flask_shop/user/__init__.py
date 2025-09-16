from flask import Blueprint
# 创建用户蓝图
user = Blueprint('user',__name__,url_prefix='/user')

from flask_shop.user import view