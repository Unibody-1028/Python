from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from mypy.types import names
from sqlalchemy.orm import backref

app = Flask(__name__)

# 数据库变量
HOST = 'localhost'
PORT = 3306
DATA_BASE = 'test'
USER = 'root'
PWD = '123456'
DB_URI = f'mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DATA_BASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭修改跟踪，提高性能
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

# 连接数据库
db = SQLAlchemy(app)

# 创建模型类
class User(db.Model):
    __tablename__ = 't_user' # 可以不写
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32))

    def __repr__(self):
        return f'<User: id={self.id} name={self.name}>'

class News(db.Model):
    __tablename__ = 't_news'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.String(100))
    uid = db.Column(db.Integer,db.ForeignKey('t_user.id'))

    user = db.relationship('User',backref=db.backref('news',lazy=True))

    def __repr__(self):
        return f'<News: id={self.id} content={self.content}>'



# 增加数据
def add_data():
    with app.app_context():
        user = User(name='bob')
        news = News(content='python')
        user.news.append(news)
        db.session.add(user)
        db.session.commit()
# 查询单表数据
def query_data():
    with app.app_context():
        users = User.query.all()
        print(users)

# 查询多表数据
def query_data_many():
    with app.app_context():
        rs = db.session.query(User,News).join(News,News.uid==User.id).all()
        print(rs)

# 更新数据
def updata_data():
    with app.app_context():
        user = User.query.first()
        user.name = 'jack'
        print(user)
        db.session.commit()


if __name__ == '__main__':
    # with app.app_context():
    #     # 在上下文中创建/删除表
    #     db.drop_all()
    #     db.create_all()

    # add_data()
    # query_data()
    # query_data_many()
    updata_data()