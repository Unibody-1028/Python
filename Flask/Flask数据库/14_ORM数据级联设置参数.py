from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship,backref

from Flask.Flask数据库.db_util import engine
from db_util import Base,Session

class User(Base):
    __tablename__ = 't_user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32))
    # articles = relationship('Article', backref='user',cascade='')
    # cascade为空时,无任何级联操作

    # articles = relationship('Article',backref='user',cascade='save-update')
    # 默认值为save-update,merge,即保存/更新主表时,自动保存/更新子表

    # articles = relationship('Article',backref='user',cascade='save-update,delete')
    # delete可以实现删除字表数据

    #articles = relationship('Article',backref='user',cascade='save-update,delete,delete-orphan',single_parent=True)
    # 当关联关系解除时,字表关系会被清空



class Article(Base):
    __tablename__ = 't_article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(32))
    uid = Column(Integer, ForeignKey('t_user.id'))

    #user = relationship('User',backref='articles',cascade='save-update,delete')
    # 会把主表的数据删除

    user = relationship('User',backref=backref('articles',cascade='save-update,delete'))
    # 相当于将级联关系建立在User表


    '''
    每个Article对象可以可以通过user属性访问对应的User对象,
    通过backref参数,在User模型中自动生成articles属性,用于访问该用户的所有作品
    '''

def add_data():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # 初始化数据

    user = User(name='SXT')
    art1 = Article(title='Python教程',uid=1)
    art2 = Article(title='JAVA实战',uid=1)
    user.articles.append(art1)
    user.articles.append(art2)

    # 保存数据
    with Session() as session:
        session.add(user)
        session.commit()


def delete_data():
    with Session() as session:
        user = session.query(User).first()
        session.delete(user)
        session.commit()

def delete_art():
    with Session() as session:
        art = session.query(Article).first()
        session.delete(art)
        session.commit()



def update_data():
    with Session() as session:
        user = session.query(User).first()
        user.articles = []
        session.commit()



if __name__ == '__main__':
    add_data()
    # delete_data()
    # update_data()
    delete_art()