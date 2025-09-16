from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser
import json

app = Flask(__name__)
api = Api(app)


class RegisterView(Resource):
    def post(self):
        # 打印所有请求信息（用于调试）
        print("===== 接收到请求 =====")
        print("请求方法:", request.method)
        print("请求URL:", request.url)
        print("Content-Type:", request.content_type)
        print("原始请求体:", repr(request.get_data()))  # 打印原始数据，包括空值
        print("======================")

        # 检查Content-Type
        if request.content_type != 'application/json':
            return {
                'msg': '请设置请求头 Content-Type: application/json',
                'error': 'Invalid Content-Type'
            }, 415

        # 尝试解析JSON数据
        try:
            json_data = request.get_json()
            if not json_data:
                return {'msg': '请求体为空，请传入有效的JSON数据'}, 400
        except json.JSONDecodeError as e:
            return {
                'msg': f'JSON格式错误：{str(e)}',
                'hint': '请检查是否用双引号、括号是否闭合'
            }, 400

        # 解析参数
        parser = RequestParser()
        parser.add_argument('uname', type=str, required=True, help='用户名格式错误或缺失')
        parser.add_argument('password', type=str, required=True, help='密码格式错误或缺失')

        try:
            args = parser.parse_args()
            return {'msg': '注册成功', 'username': args['uname']}, 201
        except Exception as e:
            return {'msg': str(e)}, 400


api.add_resource(RegisterView, '/register/')

if __name__ == '__main__':
    app.run(debug=True, port=8088, host='0.0.0.0')  # 确保本地可访问
