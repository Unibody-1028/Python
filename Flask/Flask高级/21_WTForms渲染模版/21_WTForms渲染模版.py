from flask import Flask, render_template
from forms_check import LoginForm

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'


@app.route('/login/')
def login():
    form = LoginForm()
    return render_template('login.html',form=form)


if __name__ == '__main__':
    app.run(debug=True,port=8088)





