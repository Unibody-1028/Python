from flask import Flask
from werkzeug.routing import BaseConverter
app = Flask(__name__)

class PhoneConverter(BaseConverter):
    regex = "1[3-9]\d{9}"

app.url_map.converters['phone'] = PhoneConverter


@app.route('/')
def index():
    return 'Hello'


@app.route('/<phone:param>')
def phone(param):
    print(param)
    return f'您传递的手机号是{param}'


if __name__ == '__main__':
    app.run(debug=True)