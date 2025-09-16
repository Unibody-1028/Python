from flask import Flask, request, render_template,session
from random import randint
from formscheck_20 import LoginForm


app = Flask(__name__)

# app.config["SECRET_KEY"] = ('finalfancty')
app.secret_key = 'FinalFancy'


@app.route('/')
def index():
    return 'Hello'


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        code = randint(1000,9999)
        session['code'] = str(code)
        return render_template('20_login.html',code=code)
    else:
        form = LoginForm(request.form)

        if form.validate():
            return '验证成功'
        else:
            return f'验证失败{form.errors}'


if __name__ == '__main__':
    app.run(debug=True,port=8088)