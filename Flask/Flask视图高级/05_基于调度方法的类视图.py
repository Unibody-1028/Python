from flask import Flask, typing as ft, url_for,request,render_template
from flask.views import MethodView
app = Flask(__name__)

# @app.route('/login/',methods=['GET','POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('login05.html')
#     elif request.method == 'POST':
#         uname = request.form.get('uname')
#         pwd = request.form.get('pwd')
#         print(uname)
#         print(pwd)
#         if uname == 'zs' and pwd =='123':
#             return '登录成功'
#         else:
#             return render_template('login05.html')




class LoginView(MethodView):
    def get(self):
        return render_template('login05.html')
    def post(self):
        uname = request.form.get('uname')
        pwd = request.form.get('pwd')
        print(uname)
        print(pwd)
        if uname == 'zs' and pwd =='123':
            return '登录成功'
        else:
            return render_template('login05.html',msg='用户名或密码错误')




app.add_url_rule(rule='/login/',view_func=LoginView.as_view('login'))

with app.test_request_context():
    print(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True,port=8088)