from flask import Flask
import json
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # 不转换为ASCII码

# 返回字符串
@app.route('/str1/')
def str1():
    return 'Hello-你好'
# flask将字符串转为html

#返回json
@app.route('/json1/')
def json1():
    return  json.dumps({'lang':'python语言'},ensure_ascii=False)
@app.route('/json2/')
def json2():
    return  json.dumps({'lang':'python语言JSON2'},ensure_ascii=False)

#返回元组
@app.route('/tuple1')
def tuple1():
    return '1'

@app.route('/tuple2')
def tuple2():
    #return '1,2' ,309
    return '2',309

@app.route('/tuple3')
def tuple_response3():
    # 返回JSON格式内容、状态码和响应头
    data = {'status': 'success', 'message': '操作完成'}
    json_data = json.dumps(data, ensure_ascii=False)  # 处理中文
    return json_data, 200, {'Content-Type': 'application/json'}
@app.route('/tuple4')
def tuple_response4():
    # 返回JSON格式内容、状态码和响应头
    data = {'status': 'success', 'message': '操作完成'}
    json_data = json.dumps(data, ensure_ascii=False)  # 处理中文
    return json_data, 200, [('Content-Type', 'application/json'),('lang','py')]

if __name__ == '__main__':
    app.run(debug=True,port=8088)


