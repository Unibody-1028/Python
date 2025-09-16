from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base,sessionmaker
# 数据库变量
HOST = 'localhost'
PORT = 3306
DATA_BASE = 'test'
USER = 'root'
PWD = '123456'

DB_URI = f'mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DATA_BASE}'
# 创建引擎连接数据库
engine = create_engine(DB_URI)

# 创建一个基类
Base = declarative_base()

class Person(Base):
    __tablename__ = 't_person'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32),nullable=False)
    age = Column(Integer,default=0)
    country = Column(String(32),comment='国家')

# 映射表结构
Base.metadata.create_all(engine)

