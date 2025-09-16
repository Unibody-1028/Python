from flask import Flask,render_template

app = Flask(__name__,template_folder='templates1')

# 模版的默认查找目录是templates
# 可以通过template_folder手动指定模版的查找目录


@app.route('/')
def index():
    return render_template('index19.html')

if __name__ == '__main__':
    app.run(debug=True,port=8088)


