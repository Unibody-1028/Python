from wtforms import Form,StringField,IntegerField,BooleanField,SelectField
from wtforms.validators import Length,InputRequired


class LoginForm(Form):
    uname = StringField('用户名',validators=[Length(min=1,max=10)])
    age = IntegerField('年龄',validators=[InputRequired()])
    remember = BooleanField('记住我:')
    address = SelectField('地址',choices=['北京','上海','广州'])
