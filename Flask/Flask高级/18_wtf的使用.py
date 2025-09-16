from flask import Flask, request, render_template
from wtforms import Form,StringField
from wtforms.validators import Length,EqualTo

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'


class RegisterForm(Form):
    uname = StringField(validators=[Length(min=2,max=10,message='用户名长度需要在2-10之间')])
    pwd = StringField(validators=[Length(min=6, max=16,message='密码长度需要在6-16之间')])
    pwd2 = StringField(validators=[Length(min=6, max=16, message='密码长度需要在6-16之间'),EqualTo('pwd',message='两次输入的密码不一致,请检查后重新输入')])

@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('17_register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            return '验证成功'
        else:
            return f'验证失败{form.errors}'


if __name__ == '__main__':
    app.run(debug=True,port=8088)

