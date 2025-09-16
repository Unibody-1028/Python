from werkzeug.routing import UUIDConverter
from wtforms import Form,StringField,IntegerField
from wtforms.fields.simple import URLField
from wtforms.validators import Email, InputRequired, NumberRange, Regexp,UUID,URL


class RegisterForm(Form):
    email = StringField(validators=[Email()])
    uname = StringField(validators=[InputRequired()])
    age = IntegerField(validators=[NumberRange(min=0,max=150)])
    phone = StringField(validators=[Regexp('^1[3456789]\d{9}$')])
    homepage = StringField(validators=[URL()])
    uuid = StringField(validators=[UUID()])

