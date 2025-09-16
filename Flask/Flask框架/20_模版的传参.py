from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index20.html',info='Flask模版',arg='python')
@app.route('/index')
def index2():
    return render_template('index20.html',info='Flask模版2',arg='python2')

@app.route('/home')
def home():
    context={
        'uname':'Jack',
        'pwd':123,
        'age':22,
        'offers':{'shanghai':10000,'beijing':12000,'xian':9000}
    }
    return render_template('index20.html',**context)


if __name__ == '__main__':
    app.run(debug=True,port=8088)


