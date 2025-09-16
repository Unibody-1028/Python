from sqlalchemy import Column, Integer, String, Text, ForeignKey

from Flask.Flask数据库.db_util import engine, Session
from db_util import Base



class User(Base):
    __tablename__ = 't_user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    uname = Column(String(50),nullable=False,name='name')
class News(Base):
    __tablename__ = 't_news'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    content = Column(Text,nullable=False)
    uid = Column(Integer,ForeignKey('t_user.id'))

def add_data():
    user = User(uname='sxt')
    news1 = News(title='python',content='flask',uid=1)
    news2 = News(title='mysql',content='sql',uid=1)
    with Session() as session:
        session.add(user)
        session.commit()
    with Session() as session:
        session.add(news1)
        session.add(news2)
        session.commit()

if __name__ == '__main__':
    #Base.metadata.create_all(engine)
    add_data()




