from flask import Flask, render_template

app = Flask(__name__,static_folder='demo/static')

@app.route('/')
def index():
    return 'Hello'

@app.route('/homebase/')
def homebase():
    return render_template('home_base.html')
@app.route('/register/')
def register():
    return render_template('register.html')

@app.route('/login/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True,port=8088)

