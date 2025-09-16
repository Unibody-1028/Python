# 导入所需模块
from requests import session  # 注意：此处导入的session未使用，可考虑删除
from sqlalchemy import Column, Integer, String, Text, ForeignKey
# 从自定义工具模块导入数据库引擎、会话和基类
from Flask.Flask数据库.db_util import engine
from sqlalchemy.orm import relationship  # 用于定义模型间关系
from db_util import Session, Base  # Session是会话工厂，Base是模型基类


# 定义用户模型（主表）
class User(Base):
    __tablename__ = 't_user'  # 数据库表名

    # 定义字段
    id = Column(
        Integer,
        primary_key=True,  # 主键
        autoincrement=True  # 自增
    )
    uname = Column(
        String(50),
        nullable=False,  # 非空约束
        name='name'  # 数据库中实际列名为'name'（与模型属性名uname区分）
    )

    # 一对多关系：一个用户可以有多个新闻
    # 此处注释了正向关系定义，因为在子表中用backref自动生成了反向关系
    # news = relationship('News')

    # 定义实例的字符串表示（方便打印调试）
    def __repr__(self):
        return f'<(User, id={self.id}, uname={self.uname})>'


# 定义新闻模型（从表）
# 一对多关系中，外键需要定义在"多"的一边（即每个新闻都关联一个用户）
class News(Base):
    __tablename__ = 't_news'  # 数据库表名

    # 定义字段
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    title = Column(
        String(50),
        nullable=True  # 允许标题为空
    )
    content = Column(
        Text,  # 长文本类型，适合存储文章内容
        nullable=False  # 内容不允许为空
    )
    uid = Column(
        Integer,
        ForeignKey('t_user.id')  # 外键：关联用户表的id字段
    )

    # 定义与User的反向关系：
    # 1. 每个News实例通过user属性可以访问对应的User实例
    # 2. backref='news'表示在User模型中自动生成news属性，用于访问该用户的所有新闻
    user = relationship('User', backref='news')

    # 定义实例的字符串表示
    def __repr__(self):
        return f'<(News, id={self.id}, title={self.title}, content={self.content}, uid={self.uid})>'


# 向数据库添加测试数据
def add_data():
    # 创建用户实例（uname为'sxt'）
    user = User(uname='sxt')
    # 创建两个新闻实例，uid=1表示关联id=1的用户（需确保用户已存在或先添加用户）
    news1 = News(title='python', content='flask', uid=1)
    news2 = News(title='Mysql', content='SQL', uid=1)

    # 先添加用户（使用with语句自动管理会话生命周期）
    with Session() as session:
        session.add(user)
        session.commit()  # 提交事务，保存用户到数据库

    # 再添加新闻（分两个会话是示例，实际可在一个会话中完成）
    with Session() as session:
        session.add(news1)
        session.add(news2)
        session.commit()  # 提交事务，保存新闻到数据库


# 查询所有新闻数据
def query_data():
    with Session() as session:
        # 查询t_news表的所有记录，返回News实例列表
        news = session.query(News).all()
        print(news)  # 打印所有新闻（调用News的__repr__方法）


# 通过子表（新闻）查询主表（用户）的数据
def query_data2():
    with Session() as session:
        # 获取第一条新闻记录
        news1 = session.query(News).first()
        # 通过News的user属性（由relationship定义）访问关联的用户信息
        print(news1.user)  # 打印该新闻对应的用户（调用User的__repr__方法）


# 通过主表（用户）查询子表（新闻）的数据
def query_data3():
    with Session() as session:
        # 获取第一个用户记录
        user1 = session.query(User).first()
        # 通过User的news属性（由backref自动生成）访问该用户的所有新闻
        print(user1.news)  # 打印该用户的所有新闻（列表形式）


# 程序入口
if __name__ == '__main__':
    # 以下是功能开关，取消注释对应行即可执行相应操作
    # Base.metadata.create_all(bind=engine)  # 创建数据表（首次运行时需要）
    # add_data()  # 添加测试数据
    # query_data()  # 执行查询所有新闻
    # query_data2()  # 执行通过新闻查用户
    query_data3()  # 执行通过用户查新闻