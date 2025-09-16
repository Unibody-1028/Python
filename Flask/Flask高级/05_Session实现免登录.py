from flask import Flask, render_template, request, url_for, session, redirect
from flask import views
app = Flask(__name__)
app.secret_key = 'finalfancty'

@app.route('/')
def home():
    return 'Hello'

class LoginView(views.MethodView):
    def __jump(self,msg=None):
        return render_template('login.html',msg=msg)

    def get(self):
        msg = request.args.get('msg')
        print(msg)
        return self.__jump(msg=msg)

    def post(self):
        uname = request.form.get('uname')
        pwd = request.form.get('pwd')


        if uname =='zs' and pwd == '123':
            # 记录用户信息
            session['uname'] = uname
            return render_template('index.html')

        return self.__jump(msg='用户名或密码错误')

app.add_url_rule('/login/',view_func=LoginView.as_view('login'))
@app.route('/index')
def index():
    #
    uname = session.get('uname')
    if  uname:
        return render_template('index.html')
    else:
        return redirect(url_for('login',msg='请先登录'))




with app.test_request_context():
    print(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True,port=8088)


