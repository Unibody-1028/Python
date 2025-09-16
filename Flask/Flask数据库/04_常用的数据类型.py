import enum
from datetime import date, datetime, time

from sqlalchemy import create_engine, Column, Integer, String, Float, String, Boolean, Enum, Date, DateTime, Text, \
    DECIMAL, Time
from sqlalchemy.orm import sessionmaker, declarative_base

# 数据库设置
HOST = 'localhost'
PORT = 3306
DATA_BASE = 'test'
USER = 'root'
PWD = '123456'

DB_URI = f'mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DATA_BASE}'

engine = create_engine(DB_URI)
Base = declarative_base()
session1 = sessionmaker(engine)


class TagEnum(enum.Enum):
    Python = 'Python'
    JAVA = 'JAVA'


class News(Base):
    __tablename__ = 't_news'
    id = Column(Integer, autoincrement=True, primary_key=True)
    price1 = Column(Float)
    price2 = Column(DECIMAL)
    title = Column(String(32))
    is_delete = Column(Boolean)
    tag1 = Column(Enum('Python', 'JAVA'))
    tag2 = Column(Enum(TagEnum))
    create_time = Column(Date)
    update_time = Column(DateTime)
    delete_time = Column(Time)
    content = Column(Text)


def add_data():
    news1 = News(
        price1=1234.567890,
        price2=1234.567890,
        title='SQLAlchemy测试数据',
        is_delete=True,
        tag1='Python',
        tag2='JAVA',
        create_time=date(2020, 1, 1),
        update_time=datetime(2020, 2, 1, 0, 0, 0),
        delete_time=time(0, 0, 1),
        content='测试内容'
    )
    with session1() as session:
        session.add(news1)
        session.commit()
        print('数据添加成功')


if __name__ == '__main__':
    #Base.metadata.create_all(bind=engine)
    add_data()