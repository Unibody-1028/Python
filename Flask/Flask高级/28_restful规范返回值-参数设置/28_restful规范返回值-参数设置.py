from flask import Flask
from flask_restful import Api,Resource,fields,marshal_with

app = Flask(__name__)
api = Api(app)

class News:
    def __init__(self,code,msg,info):
        self.code = code
        self.msg = msg
        self.info = info

class NewsView(Resource):
    resource_fields = {
        'code':fields.Integer(default=200),# 通过default参数设置默认值,优先级低于对象里的默认值
        'msg':fields.String,
        'content':fields.String(attribute='info') # 重新设置字段名称
    }
    @marshal_with(resource_fields)
    def get(self):
        news = News(200,'访问成功','mobile')
        return news
    @marshal_with(resource_fields)
    def post(self):
        return {'msg':'访问成功','info':'mobile'}

api.add_resource(NewsView,'/news/')

if __name__ == '__main__':
    app.run(debug=True,port=8088)


