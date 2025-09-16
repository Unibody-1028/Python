from random import randint

from sqlalchemy import Column, Integer, String

from Flask.Flask数据库.db_util import Base, Session, engine


class News(Base):
    __tablename__ = 't_news'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(32),nullable=False)
    content = Column(String(32),nullable=False)
    read_count = Column(Integer)

    def __repr__(self):
        return f'<User: id={self.id} title={self.title} content={self.content} read_count={self.read_count}>'

def add_data():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session() as session:
        for i in range(1,11):
            news = News(title=f'title{i}',content=f'info{i}',read_count=randint(1,1000))
            session.add(news)
        session.commit()

def query_by_limit():
    with Session() as session:
        news = session.query(News).limit(3).all()
        for n in news:
            print(n)

def query_by_offset():
    with Session() as session:
        news = session.query(News).offset(5).all()
        for n in news:
            print(n)

def query_by_slice():
    with Session() as session:
        news = session.query(News).slice(5,11).all()
        for n in news:
            print(n)


if __name__ == '__main__':
    # add_data()
    # query_by_limit()
    # query_by_offset()
    query_by_slice()