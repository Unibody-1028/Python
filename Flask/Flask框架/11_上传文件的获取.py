from flask import Flask,request

app = Flask(__name__)

@app.route('/upload',methods=['POST'])
def upload():

    f = request.files.get('pic')
    fname = f.filename
    with open(f'./imgs/{fname}','wb') as tf:
        tf.write(f.read())

    return f"上传成功"

if __name__ == '__main__':
    app.run(debug=True,port=8000)

