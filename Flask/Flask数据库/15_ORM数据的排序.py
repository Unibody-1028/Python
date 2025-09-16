from random import randint

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from Flask.Flask数据库.db_util import engine
from db_util import Session,Base

class User(Base):
    __tablename__ = 't_user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)

    def __repr__(self):
        return f'<User: id={self.id} name={self.name} age={self.age}>'
class News(Base):
    __tablename__ = 't_news'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(32),nullable=False)
    content = Column(String(32),nullable=False)
    read_count = Column(Integer)

    uid = Column(Integer,ForeignKey('t_user.id'))
    user = relationship('User',backref=backref('news',order_by=read_count.desc()))

    def __repr__(self):
        return f'<News: id={self.id} uid={self.uid} title={self.title} content={self.content} read_count={self.read_count}>'


def add_data():
    with Session() as session:
        for i in range(10):
            user = User(name=f'name{i+1}',age=randint(5,30))
            session.add(user)
            for i in range(randint(1,8)):
                news = News(title=f'title{i+1}',content=f'info{i}',read_count=randint(1,100))
                user.news.append(news)

        session.commit()

def query_user():
    with Session() as session:
        users = session.query(User).order_by(User.age.desc()).all()
        for u in users:
            print(u)

def query_news():
    with Session() as session:
        #news = session.query(News).order_by(News.read_count).all()
        users = session.query(User).all()
        news = users[-1].news
        for n in news:
            print(n)


if __name__ == '__main__':
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    # add_data()
    #query_user()
    query_news()