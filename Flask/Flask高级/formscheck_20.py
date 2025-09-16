from flask import session
from wtforms import Form,StringField
from wtforms.validators import Length, ValidationError

class LoginForm(Form):
    code = StringField(validators=[Length(4,4)])

    def validate_code(self,field):

        font_data = field.data
        sever_code = session.get('code')

        print(f'前端的数据:{font_data},类型{type(font_data)}')
        print(f',后端的数据:{sever_code},类型{type(sever_code)}')

        if font_data != sever_code:
            raise ValidationError('验证码错误')