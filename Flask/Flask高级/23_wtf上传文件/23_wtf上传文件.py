from flask import Flask, request, render_template
import os
from forms_check import UploadForm
from werkzeug.datastructures import CombinedMultiDict
from werkzeug.utils import secure_filename


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
        form = UploadForm(CombinedMultiDict([request.form,request.files]))
        if form.validate():
            img_file = form.pic.data
            file_name = secure_filename(img_file.filename)
            img_file.save(os.path.join(UPLOAD_PATH,file_name))

            return '上传文件成功!'
        else:
            return f'{form.errors}'

if __name__ == '__main__':
    app.run(debug=True,port=8088)

