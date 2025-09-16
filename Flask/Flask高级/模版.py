from flask import Flask, typing as ft, url_for
from flask.views import View
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

class ListView(View):
    def dispatch_request(self) -> ft.ResponseReturnValue:
        return "Hello"
app.add_url_rule(rule='/home',view_func=ListView.as_view('mylist'))

with app.test_request_context():
    print(url_for('mylist'))

if __name__ == '__main__':
    app.run(debug=True,port=8088)

