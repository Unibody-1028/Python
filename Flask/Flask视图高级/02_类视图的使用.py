from flask import Flask, typing as ft, url_for
from flask.views import View
app = Flask(__name__)

@app.route('/')
def index():
    print(url_for('mylist'))
    return 'Hello'

class ListView(View):
    def dispatch_request(self) -> ft.ResponseReturnValue:
        return '返回了一个list内容'
app.add_url_rule('/list',view_func=ListView.as_view('mylist'))
# 用于测试
with app.test_request_context():
    print(url_for('mylist'))

if __name__ == '__main__':
    app.run(debug=True,port=8088)