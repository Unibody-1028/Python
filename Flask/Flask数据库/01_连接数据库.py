from sqlalchemy import create_engine
from sqlalchemy import text
# 数据库变量
HOST = 'localhost'
PORT = 3306
DATA_BASE = 'itbz'
USER = 'root'
PWD = '123456'

# DB_URI = f'数据库名+驱动名://{USER}:{PWD}@{HOST}:{PORT}/{DATA_BASE}'
DB_URI = f'mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DATA_BASE}'
# 创建一个引擎连接数据库
engine = create_engine(DB_URI)
# 编写SQL
sql = text('show tables;')
# 连接数据库

with engine.connect() as conn:
    # 执行SQL
    rs = conn.execute(sql)
    print(rs.fetchall())
