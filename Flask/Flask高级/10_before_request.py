from flask import Flask, g, session, request

app = Flask(__name__)
app.secret_key = 'final'  # 用于 session 加密，生产环境需使用更复杂的密钥


@app.before_request
def before_request():
    # 每次请求前检查 session 中的登录状态
    uname = session.get('uname')
    if uname:
        g.uname = uname  # 存入 g 对象，供视图函数使用
    print('每次请求执行前执行的逻辑')


@app.route('/home/')
def home():
    # 通过 g.uname 判断登录状态
    if hasattr(g, 'uname'):
        return f'用户已登录,用户名为:{g.uname}'
    else:
        return '用户没有登录'


@app.route('/login/', methods=['GET', 'POST'])  # 支持 GET 显示表单，POST 提交数据
def login():
    if request.method == 'POST':
        # 实际场景中应从表单获取并验证账号密码
        uname = request.form.get('uname', 'bob')  # 简化：默认使用 'bob'
        session['uname'] = uname  # 登录成功，写入 session
        return f'登录成功，用户：{uname}'
    # GET 请求返回登录表单
    return '''
        <form method="post">
            用户名：<input type="text" name="uname">
            <input type="submit" value="登录">
        </form>
    '''


@app.route('/logout/')
def logout():
    # 清除 session 中的登录状态
    session.pop('uname', None)
    return '已登出，请重新登录'


if __name__ == '__main__':
    app.run(debug=True, port=8088)
