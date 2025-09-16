from flask import Flask, Blueprint, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index10.html')

from user import user_bp

app.register_blueprint(user_bp,url_prefix='/user')


if __name__ == '__main__':
    app.run(debug=True,port=8088)


