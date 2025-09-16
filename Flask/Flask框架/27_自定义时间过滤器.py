from flask import Flask, render_template
from datetime import datetime
import math

app = Flask(__name__)


@app.template_filter('timeFilter')
def timeFilter(value):
    value = value.replace('-','/')
    return value
@app.template_filter('handler_time')
def handler_time(time):
    '''
    处理时间
    '''
    # 获取当前时间
    now = datetime.now()
    # 将相差的时间转为秒
    temp_stamp = (now-time).total_seconds()
    if temp_stamp < 60:
        return '1分钟之前'
    elif temp_stamp>=60 and temp_stamp <60*60:
        return '1小时之前'
    elif temp_stamp>=60*60 and temp_stamp<24*60*60:
        return f'{math.floor(temp_stamp/(60*60))}小时之前'
    elif temp_stamp>=24*60*60 and temp_stamp<=30*24*60*60:
        return f'{math.floor(temp_stamp/(24*60*60))}天之前'
    else:
        return '很久以前'

@app.route('/')
def index():
    info = '2025-8-28'
    time = datetime(2025, 8, 28, 0, 0, 0, 0)
    return render_template('index27.html',info=info,time=time)


if __name__ == '__main__':
    app.run(debug=True,port=8088)





