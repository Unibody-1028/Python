from random import randint

from sqlalchemy import Column, Integer, String, ForeignKey,func
from sqlalchemy.orm import relationship

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
    user = relationship('User',backref='news')

    def __repr__(self):
        return f'<News: id={self.id} title={self.title} content={self.content} read_count={self.read_count} uid={self.uid} >'

def add_data():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with Session() as session:
        for i in range(2):
            user = User(name=f'name{i+1}',age=randint(1,60))
            session.add(user)
        for i in range(10):
            news = News(title=f'title{i+1}',content=f'info{i+1}',read_count=randint(1,1000),uid=randint(1,2))
            session.add(news)

        session.commit()

def query_join():
    # 找到所有的用户,按照发布新闻的数量排序
    '''
    select u.name,count(n.id)
    from t_user u join t_news n on u.id = n.id
    group by u.id
    order by count(n.id);
    '''
    with Session() as session:
        rs = session.query(User.name,func.count(News.id)).join(News).group_by(User.id).order_by(func.count(News.id)).all()
        print(rs)

if __name__ == '__main__':
    # add_data()
    query_join()