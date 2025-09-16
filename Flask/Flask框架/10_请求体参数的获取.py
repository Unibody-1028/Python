from flask import Flask,request

app = Flask(__name__)

@app.route('/login',methods=['POST','GET'])
def login():

    # 方式1:
    # uname = request.form.get('uname')
    # pwd = request.form.get('pwd')

    #方式2:
    uname = request.values.get('uname')
    pwd = request.values.get('pwd')


    return f'Hello,{uname},{pwd}'

if __name__ == '__main__':

    app.run(debug=True)