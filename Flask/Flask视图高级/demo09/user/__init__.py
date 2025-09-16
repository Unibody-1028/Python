from flask import Blueprint

# 创建蓝图
user_bp = Blueprint('user',__name__)

from user import view
