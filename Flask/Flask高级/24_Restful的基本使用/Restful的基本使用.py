from flask import Flask, url_for
from flask_restful import Resource
from flask_restful import Api

app = Flask(__name__)
# 建立Api对象并绑定app
api =Api(app)


class LoginView(Resource):
    def get(self):
        return {'flag':True}

    def post(self):
        return {'flag':False}

# 建立路由映射
api.add_resource(LoginView,'/login/','/login2/',endpoint='login')

with app.test_request_context():
    # 没有写endpoint时,反向url_for函数通过小写函数使用,有多个url时,返回第一个
    print(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True,port=8088)


