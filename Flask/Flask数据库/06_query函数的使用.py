from random import randint
from sqlalchemy import Column,Integer,String,func
from db_util import Session
from Flask.Flask数据库.db_util import engine
from db_util import Base

class Item(Base):
    __tablename__ = 't_item'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(32))
    price = Column(Integer)

def add_data():
    with Session() as session:
        for i in range(10):
            item = Item(title=f"产品{i+1}",price=randint(1,100))
            session.add(item)
        session.commit()
    print('数据添加成功')

def query_data():
    with Session() as session:
        rs = session.query(Item).all()
        for r in rs:
            print(f'{r.id}--{r.title}--{r.price}')

def query_data_attr():
    with Session() as session:
        rs = session.query(Item.id,Item.title).all()
        for r in rs:
            print(f'{r.id}--{r.title}')

def query_by_func():
    with Session() as session:
        rs = session.query(func.count(Item.id)).first()
        print(rs)
        rs = session.query(func.max(Item.price)).first()
        print(rs)

if __name__ == '__main__':
    #Base.metadata.create_all(engine)
    #add_data()
    #query_data()
    #query_data_attr()
    query_by_func()