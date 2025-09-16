from flask import Flask
from flask_restful import Api, Resource
from user import user_bp


app = Flask(__name__)
api = Api(user_bp)

class LoginView(Resource):
    def get(self):
        return {'msg':'注册成功'}
# 建立映射关系
api.add_resource(LoginView,'/login/')