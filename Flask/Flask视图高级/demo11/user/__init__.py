from flask import Blueprint

# 设置静态文件路径
user_bp = Blueprint('user',__name__,static_folder='static')

from user import view
