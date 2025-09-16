from flask import Flask
from blinker import default_namespace
app = Flask(__name__)

@app.route('/')
def index():
    fire_signal.send()
    return 'Hello'

# 1.定义信号
space = default_namespace
fire_signal = space.signal('发送一个信号')
# 2.监听信号
def start_func(sender):
    print('start_func开始执行')
fire_signal.connect(start_func)
# 3.发送信号
#fire_signal.send()


if __name__ == '__main__':
    app.run(debug=True,port=8088)


