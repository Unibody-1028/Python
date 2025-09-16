from flask import Flask, typing as ft, url_for, render_template
from flask.views import View
app = Flask(__name__)


class BaseView(View):
    def __init__(self):
        self.msg = {
            'login':'这是login页面的信息123',
            'register':'这是register页面的信息'
        }

class LoginView(BaseView):
    def dispatch_request(self) -> ft.ResponseReturnValue:
        #my_msg = '这是一个登录功能'
        self.msg['my_msg'] = '这是一个登录功能'
        # return render_template('login.html',msg=self.msg.get('login'),my_msg=my_msg)
        # 将多个参数适用字典一起传递
        return render_template('login.html',**self.msg)

class RegisterView(BaseView):
    def dispatch_request(self) -> ft.ResponseReturnValue:
        #my_msg = '这是一个注册功能'
        self.msg['my_msg'] = '这是一个注册功能'
        return render_template('register.html',**self.msg)


app.add_url_rule(rule='/login/',view_func=LoginView.as_view('login'))
app.add_url_rule(rule='/register/',view_func=RegisterView.as_view('register'))


with app.test_request_context():
    print(url_for('login'))
    print(url_for('register'))

if __name__ == '__main__':
    app.run(debug=True,port=8088)



