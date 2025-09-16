from flask import Blueprint

# 创建蓝图
item_bp = Blueprint('item',__name__)

# 管理的子功能
@item_bp.route('/item/')
def login():
    return '产品模块'