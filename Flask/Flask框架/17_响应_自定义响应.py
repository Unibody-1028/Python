from flask import Flask,Response,make_response

app = Flask(__name__)

@app.route('/')
def index():
    #return Response('你好',status=500,headers={'lang':'Python'})
    return Response(status=404)

@app.route('/home')
def home():
    resp = make_response('这是创建的response对象')
    resp.headers['lang'] = 'Python_home'
    resp.status = 404
    return resp


if __name__ == '__main__':
    app.run(debug=True)


