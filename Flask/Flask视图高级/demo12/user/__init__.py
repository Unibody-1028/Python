from flask import Blueprint

user_bp = Blueprint('user',__name__,static_url_path='/user_static',static_folder='user_page')
# static_url_path修改路由地址
# static_folder指定静态文件的实际存储目录

from user import view



