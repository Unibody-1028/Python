from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    url = url_for('test_url')
    return f'Hello-----{url}'

@app.route('/test/')
def test_url():
    return '为了测试请求上下文'

# with app.app_context():
#     url = url_for('test_url')
#     print(url)

with app.test_request_context():
    url = url_for('test_url')
    print(url)


if __name__ == '__main__':
    app.run(debug=True,port=8088)
