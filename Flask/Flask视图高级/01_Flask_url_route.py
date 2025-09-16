from flask import Flask, url_for

app = Flask(__name__)

@app.route('/',endpoint='index')
def index():

    print(url_for('show'))
    print(url_for('index'))
    return 'Hello'

def show_info():
    return "这是一个介绍信息"
app.add_url_rule('/index',view_func=show_info,endpoint='show') #endpoint 重新指定了show_info函数的名字
#app.route底层就是使用的add_url_rule



if __name__ == '__main__':
    app.run(debug=True,port=8088)