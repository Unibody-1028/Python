from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# 数据库设置
HOST = 'localhost'
PORT = 3306
DATA_BASE = 'test'
USER = 'root'
PWD = '123456'

DB_URI = f'mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DATA_BASE}'

engine = create_engine(DB_URI)
Base = declarative_base()

class Person(Base):
    __tablename__ = 't_person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)
    country = Column(String(32))

# 创建数据表
# Base.metadata.create_all(engine)

# 创建会话对象来操作数据
session1 = sessionmaker(bind=engine)


def create_data():
    with session1() as session:
        session.add(Person(name='李四',age=30,country='中国'))
        p1 = Person(name='job',age=20,country='us')
        session.add(p1)
        # session.add_all([p1,p2,p3......])
        session.commit()
        print('数据添加成功')

def query_data_all():
    with session1() as session:
        all_person = session.query(Person).all()
        for p in all_person:
            print(f'{p.id}--{p.name}--{p.age}--{p.country}')

def query_data_by_params():
    with session1() as session:
        #p = session.query(Person).filter_by(name='job').first() # .all()
        p = session.query(Person).filter(Person.name=='job').first() # .all()
        print(f'{p.id}--{p.name}--{p.age}--{p.country}')

def update_data():
    with session1() as session:
        p = session.query(Person).filter(Person.name == 'job').first()
        p.age = 22
        session.commit()
        print(f'{p.id}--{p.name}--{p.age}--{p.country}')

def delete_data():
    with session1() as session:
        p = session.query(Person).filter(Person.name == 'job').first()
        session.delete(p)
        session.commit()


def delete_all_data():
    with session1() as session:
        p = session.query(Person).all()
        for p1 in p:
            session.delete(p1)
        session.commit()


if __name__ == '__main__':
    #create_data()
    query_data_all()
    #query_data_by_params()
    #update_data()
    #delete_data()
    #delete_all_data()