from random import choice, randint

from sqlalchemy import Column,Integer,String,text,and_

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

    names = ['jack','bob','ash','anna']
    with Session() as session:
        for i in range(20):
            user = User(name=choice(names),age=randint(1,8))
            session.add(user)

        session.commit()

def query_data():
    # 获取一个名字为jack的用户,再获取和他同名同年龄的人
    '''
    select u.name, u.age from t_user
    where (select name,age from t_user where name='jack') as z
     z.name = u.name and z.age = u.age ;

    '''

    with Session() as session:
        sub_sql = session.query(
            User.name.label('uname'),  # 给User.name起别名uname，便于外层引用
            User.age.label('uage')  # 给User.age起别名uage，便于外层引用
        ).filter(User.name == 'bob').limit(1).subquery()  # 转为子查询

        main_sql = session.query(User).filter(
            and_(User.name == sub_sql.c.uname, User.age == sub_sql.c.uage)
        ).all()
        print(main_sql)



if __name__ == '__main__':
    # add_data()
    query_data()
