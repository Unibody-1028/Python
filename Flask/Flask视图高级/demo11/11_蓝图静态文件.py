from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


from user import user_bp
# 增加路由地址前缀

app.register_blueprint(user_bp,url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True,port=8088)


