from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with

app = Flask(__name__)
api = Api(app)

class News:
    def __init__(self,code,msg,state,context):
        self.code = code
        self.msg = msg
        self.state = state
        self.context = context

class NewsView(Resource):
    resouce_fields={
        'code':fields.Integer,
        'msg':fields.String,
        'state':fields.String
    }

    @marshal_with(resouce_fields)
    def get(self):
        return {"code":200,"msg":'访问成功'}
    @marshal_with(resouce_fields)
    def post(self):
        return {'msg':'注册成功'}
    @marshal_with(resouce_fields)
    def put(self):
        # 返回对象时,会自动在对象中获取装饰器约定好的返回值,并封装成json格式的数据返回
        news = News(200,'ok',state='mobile',context='aaa')
        return news


api.add_resource(NewsView,'/news/')
if __name__ == '__main__':
    app.run(debug=True,port=8088)


