from flask import Flask, typing as ft, url_for,request,render_template
from flask.views import MethodView
app = Flask(__name__)

'''
class LoginView(MethodView):
    def get(self,msg=None):
        return render_template('login06.html',msg=msg)
    def post(self):
        uname = request.form.get('uname')
        pwd = request.form.get('pwd')
        print(uname)
        print(pwd)
        if uname == 'zs' and pwd =='123':
            return '登录成功'
        else:
            return self.get(msg='用户名或密码错误')
'''


class LoginView(MethodView):
    def __jump(self,msg=None):
        return render_template('login06.html', msg=msg)
    def get(self,msg=None):
        return self.__jump()
    def post(self):
        uname = request.form.get('uname')
        pwd = request.form.get('pwd')
        print(uname)
        print(pwd)
        if uname == 'zs' and pwd =='123':
            return '登录成功'
        else:
            return self.__jump(msg='用户名或密码错误')



app.add_url_rule(rule='/login/',view_func=LoginView.as_view('login'))

with app.test_request_context():
    print(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True,port=8088)