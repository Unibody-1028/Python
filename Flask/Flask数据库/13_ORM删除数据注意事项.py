from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Flask.Flask数据库.db_util import Base, engine, Session


class User(Base):
    __tablename__ = 't_user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32))

class Article(Base):
    __tablename__ = 't_article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(32))
    # 设置nullable=False限制删除行为
    uid = Column(Integer, ForeignKey('t_user.id'), nullable=False)
    user = relationship('User',backref='articles')
'''
user = relationship('User', backref='articles') 是 SQLAlchemy 中定义模型间关联关系的核心配置,
用于在 ORM 层面建立 Article（文章）和 User（用户）之间的 “多对一 / 一对多” 双向关联。各个参数的详细解释如下：
1. 第一个参数：'User'（关联的目标模型）
作用：
    指定当前模型（Article）要关联的目标模型类名称（字符串形式，也可直接写类名 User，但推荐用字符串避免循环导入问题）。
含义：
    表示 Article 模型关联的是 User 模型，即 “一篇文章属于一个用户”。
对应关系：
    在数据库层面，通过 Article 表的 uid 外键（ForeignKey('t_user.id')）关联 User 表的 id 主键，而 relationship 则在 ORM 层面将这种关联转化为可直接访问的属性。
2. 第二个参数：backref='articles'（反向关联的属性名）
作用：
    在目标模型（User）中自动生成一个反向关联的属性，用于从 User 访问关联的 Article 集合。
含义：
    backref='articles' 表示：当定义 Article.user 正向关联后，SQLAlchemy 会在 User 类中自动添加一个 articles 属性。
    通过 User.articles 可以直接获取该用户发布的所有文章（返回一个列表，包含多个 Article 实例）。
双向关联逻辑：
    正向：Article → User（通过 article.user 获取文章的作者）。
    反向：User → Article（通过 user.articles 获取用户的所有文章）。
3. 隐藏的默认参数：uselist=True（一对多的关键）
    虽然代码中没有显式写出，但 relationship 有一个默认参数 uselist=True，表示关联的结果是一个列表（多个对象）。
这正是 “一对多” 关系的体现：一个 User 可以关联多个 Article，因此 user.articles 返回列表；而一个 Article 只关联一个 User，
因此 article.user 返回单个对象（uselist=False 的效果）。
'''

def add_data():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    user = User(name='SXT')
    art1 = Article(title='Python教程',uid=1)
    art2 = Article(title='JAVA实战',uid=1)

    user.articles.append(art1)
    user.articles.append(art2)
    with Session() as session:
        session.add(user)
        session.commit()

def deleta_data():
    # 默认情况下,删除主表数据时,会将字表中引用主表的外键设置为Null
    with Session() as session:
        user = session.query(User).first()
        session.delete(user)
        session.commit()



if __name__ == '__main__':
    add_data()
    deleta_data()

