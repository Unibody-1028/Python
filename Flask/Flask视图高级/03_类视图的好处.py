from logging import raiseExceptions

from flask import Flask, typing as ft, url_for, jsonify
from flask.views import View

app = Flask(__name__)
# 需求:返回的结果都必须是json数据

class BaseView(View):
    def get_data(self):
        raise NotImplementedError

    def dispatch_request(self) -> ft.ResponseReturnValue:
        return jsonify(self.get_data())

# 调用JsonView时,会调用dispatch_request函数,返回数据
class JsonView(BaseView):
    def get_data(self):
        return {'uname':'jack','age':20}

class JsonView2(BaseView):
    def get_data(self):
        return {'uname':'bob','age':22}

app.add_url_rule(rule='/base/',view_func=BaseView.as_view('base'))
app.add_url_rule(rule='/json/',view_func=JsonView.as_view('json'))
app.add_url_rule(rule='/json2/',view_func=JsonView2.as_view('json2'))


with app.test_request_context():
    print(url_for('json'))
    print(url_for('json2'))


if __name__ == '__main__':
    app.run(debug=True,port=8088)


