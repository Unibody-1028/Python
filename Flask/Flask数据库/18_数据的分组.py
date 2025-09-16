from random import randint

from sqlalchemy import Column,Integer,String,text,func
from Flask.Flask数据库.db_util import engine
from db_util import Base,Session

class User(Base):
    __tablename__ = 't_user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)

    def __repr__(self):
        return f'<User: id={self.id} name={self.name} age={self.age}>'


def add_data():
    # 1. 处理表结构（删除旧表、创建新表）
    with engine.connect() as conn:
        # 关闭外键检查
        conn.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
        # 提交事务，确保配置生效
        conn.commit()

        # 删除所有表（此时外键检查已关闭，不会报错）
        Base.metadata.drop_all(bind=conn)
        # 创建所有表
        Base.metadata.create_all(bind=conn)

        # 重新开启外键检查
        conn.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
        conn.commit()  # 再次提交事务

    # 2. 独立添加数据（使用Session）
    with Session() as session:
        for i in range(100):
            user = User(name=f'user{i + 1}', age=randint(1, 30))
            session.add(user)  # 注意：需要将用户添加到会话中
        session.commit()  # 提交数据事务

def query_data():
    # 统计每个年龄的人数有多少
    with Session() as session:
        rs = session.query(User.age,func.count(User.id)).group_by(User.age).all()
        print(rs)

def query_data2():
    # 统计每个年龄的人数有多少,并且年龄>18岁
    with Session() as session:
        rs = session.query(User.age,func.count(User.id)).group_by(User.age).having(User.age>18).all()
        print(rs)

if __name__ == '__main__':
    # add_data()
    # query_data()
    query_data2()