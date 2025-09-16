from flask import render_template
from user import user_bp

@user_bp.route('/')
def index():
    return render_template('index.html')
