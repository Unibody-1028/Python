from random import randint

from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship, backref

from Flask.Flask数据库.db_util import engine
from db_util import Base,Session

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
    user = relationship('User',backref=backref('news',lazy='dynamic'))
    def __repr__(self):
        return (f'<User: id={self.id} title={self.title} content={self.content} '
                f'read_count={self.read_count}>')


def add_data():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session() as session:
        for i in range(10):
            user = User(name=f'name{i+1}',age=randint(1,30))
            session.add(user)
        for i in range(10):
            news = News(title=f'title{i+1}',content=f'info{i+1}',read_count=randint(1,1000))
            user.news.append(news)

        session.commit()

def query_data():
    with Session() as session:
        user = session.query(User)
        print(user)
        print(type(user))

def query_data2():
    with Session() as session:
        user = session.query(User).all()[-1]
        print(user.news)
        print(type(user.news))

def query_data3():
    '''
    使用了默认的 lazy='select'（或未显式配置 lazy='dynamic'）
    当访问 user.news 时，SQLAlchemy 会立即查询并加载所有关联的新闻，返回的是 “已加载的列表”（InstrumentedList），而非可继续过滤的查询对象。
    因此调用 user.news.filter(...) 会报错 —— 列表没有 filter 方法。
    '''

    with Session() as session:
        user = session.query(User).all()[-1]
        # print(user)
        news = user.news.filter(News.read_count>500).all()
        print(news)

if __name__ == '__main__':
    #add_data()
    # query_data()
    # query_data2()
    query_data3()