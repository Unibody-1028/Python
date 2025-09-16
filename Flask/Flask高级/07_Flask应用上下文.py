from flask import Flask,current_app

app = Flask(__name__)

# 方法1
# app_ctx = app.app_context()
# app_ctx.push()
# print(current_app.name)

# 方法2
with app.app_context():
    print(current_app.name)


@app.route('/')
def index():
    return f'Hello,这是一个"{current_app.name}"应用'

if __name__ == '__main__':
    app.run(debug=True,port=8088)
