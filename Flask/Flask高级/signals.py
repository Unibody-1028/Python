from blinker import default_namespace
from flask import request,g
space = default_namespace
login_space = space.signal('登录')

def login_signal(sender):
    ip = request.remote_addr
    data = f'{ip}:{g.name}'
    with open('login.log', 'a', encoding='utf-8') as f:
        f.write(data+'\n')

# 监听信号
login_space.connect(login_signal)


