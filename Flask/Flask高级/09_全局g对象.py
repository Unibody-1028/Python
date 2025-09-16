from flask import Flask,g
from utils_old import *
import utils_new as n
app = Flask(__name__)

@app.route('/')
def index():
    uname = 'jack'
    a = func_a(uname)
    b = func_b(uname)
    c = func_c(uname)
    return f'Hello<br>{a}<br>{b}<br>{c}'

@app.route('/new/')
def new_index():
    uname = 'jack2'
    g.uname = uname
    a = n.func_a()
    b = n.func_b()
    c = n.func_c()
    return f'Hello<br>{a}<br>{b}<br>{c}'



if __name__ == '__main__':
    app.run(debug=True,port=8088)


