from wtforms import Form,FileField
from flask_wtf.file import FileAllowed,FileRequired


class UploadForm(Form):
    pic = FileField(validators=[FileRequired(),FileAllowed(['png','jpg'])])


