from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# 数据库变量
HOST = 'localhost'
PORT = 3306
DATA_BASE = 'flask_db'
USER = 'root'
PWD = '123456'
DB_URI = f'mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DATA_BASE}'

engine = create_engine(DB_URI)
Session = sessionmaker(engine)

Base = declarative_base()
