from sqlalchemy import Column, Integer, String, DateTime

from db_util import engine
from db_util import Base
from datetime import datetime
from db_util import Session

class News(Base):
    __tablename__ = 't_news2'
    id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)
    read_count = Column(Integer, default=1)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    phone = Column(String(11))

def create_table():
    Base.metadata.create_all(engine)
def add_data():
    new1 = News(
        title='Python',
        phone='13222222222'
    )
    with Session() as session:
        session.add(new1)
        session.commit()
        print('数据添加成功')

def add_data2():
    with Session() as session:
        new1 = session.query(News).first()
        new1.read_count=2
        session.commit()




if __name__ == '__main__':
    # 创建表
    #create_table()
    # 添加数据
    #add_data()
    # 修改数据
    add_data2()

