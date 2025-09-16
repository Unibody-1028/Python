from flask.blueprints import Blueprint

user_bp = Blueprint('user',__name__)

from user import views
