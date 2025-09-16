from flask import Flask,request

app = Flask(__name__)

@app.route('/args',methods=['GET','POST'])
def args():
    url = request.url
    method = request.method
    headers = request.headers.get('Content-Type')
    User_Agent = request.headers.get('User-Agent')
    cookie = request.cookies.get('uid')
    return f"Hello---URL:{url}---method:{method}---Content-Type{headers}---User_Agent{User_Agent}---Cookie:{cookie}"


if __name__ == '__main__':
    app.run(debug=True)



