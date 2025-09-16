from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    # 获取参数
    # 方式1:
    # uname = request.args.get('uname')
    # pwd = request.args.get('pwd')

    # 方式2：
    uname = request.values.get('uname')
    pwd = request.values.get('pwd')


    return f'Hello uname:{uname} pwd:{pwd}'

if __name__ == '__main__':

    app.run(debug=True)

