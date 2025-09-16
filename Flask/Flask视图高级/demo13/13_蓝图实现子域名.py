from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

from user import user_bp
app.register_blueprint(user_bp)

if __name__ == '__main__':

    # 127.0.0.1:8088
    #app.config['SERVER_NAME'] = 'flaskexample.com:8088'

    app.run(debug=True,port=8088)

