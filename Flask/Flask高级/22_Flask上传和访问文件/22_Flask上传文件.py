from flask import Flask,render_template,request,send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'imgs')


@app.route('/')
def index():
    return 'Hello'

@app.route('/upload/',methods = ['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        img_file = request.files.get('pic')
        filename = img_file.filename
        # 文件名的安全转换
        filename = secure_filename(filename)
        # 保存文件
        img_file.save(os.path.join(UPLOAD_PATH,filename))
        return '文件上传成功!!!'


@app.route('/download/<filename>/')
def download(filename):
    return send_from_directory(UPLOAD_PATH,filename)



if __name__ == '__main__':
    app.run(debug=True,port=8088)