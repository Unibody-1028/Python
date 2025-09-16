from sqlalchemy import Column,Integer,String

from Flask.Flask数据库.db_util import engine
from db_util import Base,Session

class City(Base):
    __tablename__ = 't_city'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32))
    pid = Column(Integer)

    def __repr__(self):
        return f'<City: id={self.id} name={self.name} pid={self.pid}>'

def add_data():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    city1 = City(id=1,name='河北',pid=0)
    city2 = City(id=10,name='石家庄',pid=1)
    city3 = City(id=11,name='天津',pid=1)
    city4 = City(id=2,name='广东',pid=0)
    city5 = City(id=21,name='深圳',pid=2)
    city6 = City(id=22,name='广州',pid=2)

    with Session() as ses:
        ses.add(city1)
        ses.add(city2)
        ses.add(city3)
        ses.add(city4)
        ses.add(city5)
        ses.add(city6)
        ses.commit()

def query_city():
    '''
    select c1.id , c1.name , c2.pid , c2.id
    from t_city c1
    left join t_city c2
    on c1.id == c2.pid
    '''
    with Session() as ses:
        from sqlalchemy.orm import aliased
        c = aliased(City)
        rs = ses.query(City.pid,City.name,City.id,c.pid,c.name,c.id).join(c,City.id==c.pid).all()
        print(rs)

if __name__ == '__main__':

    # add_data()
    query_city()