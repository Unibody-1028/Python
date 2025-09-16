from flask import Flask,render_template,got_request_exception

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/home/')
def home():
    num = 1/0
    return f'结果为0'
def exception_log(sender,exception):
    print(sender)
    print(exception)


got_request_exception.connect(exception_log)


if __name__ == '__main__':
    app.run(debug=True,port=8088)

