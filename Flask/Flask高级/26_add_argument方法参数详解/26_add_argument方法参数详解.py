from flask import Flask
from flask_restful import Api,Resource,inputs
from flask_restful.reqparse import RequestParser

app = Flask(__name__)
api = Api(app)

class RegisterView(Resource):
    def post(self):
        # 建立解析器
        parser = RequestParser()
        # 定义解析规则
        parser.add_argument('uname',type=str,required=True,trim=True,help='用户名格式错误')
        parser.add_argument('pwd',type=str,help='密码格式错误',default='123456')
        parser.add_argument('age',type=int,help='年龄格式错误')
        parser.add_argument('gender',type=str,choices=['男','女'],help='性别错误')
        parser.add_argument('birthday',type=inputs.date,help='生日格式错误')
        parser.add_argument('phonenumber',type=inputs.regex('^1[3456789]\d{9}$'),help='电话格式错误')
        parser.add_argument('homepage',type=inputs.url,help='homepage-url格式错误')

        # 解析数据
        args = parser.parse_args()
        print(args)
        return {'msg':'注册成功'}
api.add_resource(RegisterView,'/register/')


if __name__ == '__main__':
    app.run(debug=True,port=8088)

