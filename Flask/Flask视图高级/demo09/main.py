from flask import Flask

app = Flask(__name__)


# 注册蓝图
from user.view import user_bp
app.register_blueprint(user_bp,url_prefix='/user')

from item.view import item_bp
app.register_blueprint(item_bp,url_prefix='/goods')


if __name__ == '__main__':
    app.run(debug=True,port=8088)


