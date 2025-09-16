import json

from flask import Flask,render_template,Response
from flask_restful import Api,Resource

app = Flask(__name__)
app.config['RESTFUL_JSON'] = dict(ensure_ascii=False)
api = Api(app)

class IndexView(Resource):
    def get(self):
        return render_template('index.html')

class HomeView(Resource):
    def get(self):
        return {'msg':'个人信息'}


api.add_resource(IndexView,'/index/')
api.add_resource(HomeView,'/home/')



@api.representation('text/html')
def out_html(data,code,headers):
    # 必须返回一个response对象
    if isinstance(data,str):
        resp = Response(data)
        return resp
    else:
        return Response(json.dumps(data,ensure_ascii=False).encode('gbk'))




if __name__ == '__main__':
    app.run(debug=True,port=8088)
