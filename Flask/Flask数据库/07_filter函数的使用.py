from random import randint
from uuid import uuid4
from sqlalchemy import Column,Integer,String,Float,Text

from Flask.Flask数据库.db_util import engine
from db_util import Base,Session

class Article(Base):
    __tablename__ = 't_article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    price = Column(Float,nullable=False)
    content = Column(Text)
    # 返回实例对象的信息
    def __repr__(self):
        return f"<Article(title:{self.title}, price:{self.price}, content:{self.content})>"


def add_data():
    with Session() as session:
        for i in range(10):
            if i%2==0:
                art = Article(title=f'title{i+1}',price=randint(1,100),content=uuid4())
            else:
                art = Article(title=f'TITLE{i+1}', price=randint(1, 100))
            session.add(art)

        session.commit()

def query_data():
    with Session() as session:
        #rs = session.query(Article).filter_by(id=1).first()

        rs = session.query(Article).filter(Article.id==1).first()

        print(rs)
def query_data_like():
    with Session() as session:
        # select * from t_article where title like 'title%';
        rs = session.query(Article).filter(Article.title.like('title%')).all()
        for r in rs:
            print(r.title)

def query_data_in():
    with Session() as session:
        # select * from t_article where title like 'title%';
        rs = session.query(Article).filter(Article.title.in_(['title1','title3','title5'])).all()
        for r in rs:
            print(r.title)

if __name__ == '__main__':
    #Base.metadata.create_all(engine)
    #add_data()
    #query_data()
    # query_data_like()
    query_data_in()

