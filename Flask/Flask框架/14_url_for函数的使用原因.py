from flask import Flask,url_for

app = Flask(__name__)

@app.route('/index')
def index():
    return f'Hello'


@app.route('/show_url')
def show_url():
    url = url_for('index',next='/')
    # 会自动将/编码，不需要手动处理
    # 将 next='/' 转为 ?next=/
    '''
    自动编码特殊字符：如果参数包含空格、中文、/ 等特殊字符（比如 next='/user list'），
    url_for 会自动进行 URL 编码（转为 next=%2Fuser%20list），无需手动处理，避免 URL 语法错误。
    '''
    return f'反向查找到的URL地址为:{url}'

if __name__ == '__main__':
    app.run(debug=True)