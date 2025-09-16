from flask import Flask, render_template

app = Flask(__name__)

@app.template_filter('cut')#定义过滤器名称
def cut(value):
    value = value.replace('ab','e')
    return value
@app.route('/')
def index():
    info = 'abcab'
    return render_template('index26.html',info=info)

if __name__ == '__main__':
    app.run(debug=True,port=8088)

