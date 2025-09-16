import typing as t

from flask import Flask
from werkzeug.routing import BaseConverter
app = Flask(__name__)

# 需求：路径参数传递多信息并以一个参数接收
# 例如：获取姓名：zs 年龄：18
#user/zs+18

#自定义转换器
class LiConverter(BaseConverter):
    def to_python(self, value: str) -> t.Any:
        return value.split('+')
        # 将结果返回给user_info的info参数

#注册转换器
app.url_map.converters['li'] = LiConverter

@app.route('/')
def index():
    return 'Hello'

@app.route('/user/<info>')
def user(info):
    args = info.split('+')
    return f'姓名:{args[0]},年龄:{args[1]}'

@app.route('/user_info/<li:info>')
def user_info(info):
    return f"获取到的信息为：{info}"

if __name__ == '__main__':
    app.run(debug=True)

