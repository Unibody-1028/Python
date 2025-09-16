from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

class BaseConfig:
    DEBUG = True

class KConfig(BaseConfig):
    pass

class PConfig(BaseConfig):
    DEBUG = False

if __name__ == '__main__':
    #app.run(debug=True)

    #方式1
    #app.config['DEBUG'] = True
    # app.config.update({'DEBUG':True})
    # app.run()

    #方式2
    # app.config.from_mapping({"DEBUG":True})
    # app.run()

    #方式3
    app.config.from_object(KConfig)
    app.run()

    #方式4
    # import json
    # app.config.from_file('config.json',json.load)
    # app.run()

    #方式5
    # app.config.from_pyfile('setting.py')
    # app.run()

    # 方法6
    # 通过环境变量设置
    #app.config.from_envvar('flask_setting')
    # app.run()
