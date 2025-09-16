from flask import Flask,request,render_template
from forms_check import RegisterForm


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'
@app.route('/register/',methods=["GET","POST"])
def register():
    if request.method == 'GET':
        return render_template('19_register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():

            return '验证成功'
        else:
            return f'验证失败{form.errors}'

if __name__ == '__main__':
    app.run(debug=True,port=8088)



