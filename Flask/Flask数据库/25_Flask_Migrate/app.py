from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

HOST = 'localhost'
PORT = 3306
DATA_BASE = 'flask_db'
USER = 'root'
PWD = '123456'
DB_URI = f'mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DATA_BASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭修改跟踪，提高性能
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

db = SQLAlchemy(app)

# 创建模型类
class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32))
    age = db.Column(db.Integer)
    city = db.Column(db.String(32))

    def __repr__(self):
        return f'<User: id={self.id} name={self.name}>'

# 使用migrate同步表结构

from flask_migrate import migrate, Migrate

Migrate(app,db)



