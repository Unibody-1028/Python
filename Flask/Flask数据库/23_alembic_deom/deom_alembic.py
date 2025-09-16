from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

# 数据库变量
HOST = 'localhost'
PORT = 3306
DATA_BASE = 'test'
USER = 'root'
PWD = '123456'
DB_URI = f'mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DATA_BASE}'

engine = create_engine(DB_URI)
Base = declarative_base()

class User(Base):
    __tablename__ = 't_user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)


