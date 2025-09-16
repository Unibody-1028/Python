# 从自定义工具模块导入数据库引擎、基类和会话
from Flask.Flask数据库.db_util import engine
from db_util import Base, Session
# 导入ORM关系定义所需的工具
from sqlalchemy.orm import relationship, backref
# 导入字段类型和外键
from sqlalchemy import Column, Integer, String, Text, ForeignKey


# 登录用户模型（主表）
class LoginUser(Base):
    __tablename__ = 't_user_login1_1'  # 数据库表名，后缀1_1表示一对一关系

    # 定义字段
    id = Column(
        Integer,
        primary_key=True,  # 主键
        autoincrement=True  # 自增
    )
    uname = Column(
        String(32),
        nullable=False  # 用户名非空
    )
    passwd = Column(
        String(32),
        nullable=False  # 密码非空
    )

    # 注释的一对一关系定义（与下面User类中的定义等效，二选一即可）
    # user = relationship('User', uselist=False)  # uselist=False表示一对一（默认是一对多）

    # 定义实例的字符串表示（方便打印调试）
    def __repr__(self):
        return f'<User id={self.id}, uname={self.uname}, passwd={self.passwd}>'


# 用户详细信息模型（从表）
class User(Base):
    __tablename__ = 't_user1_1'  # 数据库表名，与登录表对应

    # 定义字段
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name = Column(
        String(32),
        nullable=False,
        name='name'  # 数据库列名与属性名一致（可省略）
    )
    gender = Column(
        String(1)  # 存储性别，如'男'/'女'
    )
    address = Column(
        String(64)  # 存储地址信息
    )
    login_id = Column(
        Integer,
        ForeignKey('t_user_login1_1.id'),  # 外键：关联登录表的id
        unique=True  # 关键：一对一关系需要外键唯一（避免一个登录用户对应多个详细信息）
    )

    # 定义与LoginUser的一对一关系：
    # 1. login_user属性：通过该属性可访问关联的登录用户信息
    # 2. backref=backref('user', uselist=False)：
    #    - 在LoginUser中自动生成user属性，用于反向访问详细信息
    #    - uselist=False强制为一对一（默认是一对多列表）
    login_user = relationship(
        'LoginUser',
        backref=backref('user', uselist=False)
    )

    # 定义实例的字符串表示
    def __repr__(self):
        return f'<User-info id={self.id}, name={self.name}, gender={self.gender}, address={self.address}>'


# 方式1：通过登录用户关联详细信息（推荐）
def add_date():
    # 创建登录用户实例
    login = LoginUser(uname='bob', passwd='123456')
    # 创建用户详细信息实例
    user = User(name='sxt', gender='男', address='北京')
    # 建立关联：登录用户的user属性指向详细信息
    login.user = user  # 利用backref生成的user属性

    # 保存到数据库
    with Session() as session:
        session.add(login)  # 添加登录用户（会自动关联保存详细信息）
        session.commit()  # 提交事务


# 方式2：通过详细信息关联登录用户
def add_date2():
    # 创建登录用户实例
    login = LoginUser(uname='jacj', passwd='123456')  # 注意：用户名jacj可能是笔误（应为jack）
    # 创建用户详细信息实例
    user = User(name='aaa', gender='女', address='北京')
    # 建立关联：详细信息的login_user属性指向登录用户
    user.login_user = login

    # 保存到数据库
    with Session() as session:
        session.add(user)  # 添加详细信息（会自动关联保存登录用户）
        session.commit()


# 查询关联数据
def query_data():
    # 示例1：通过登录用户查询详细信息（注释部分）
    # with Session() as session:
    #     login = session.query(LoginUser).first()  # 获取第一个登录用户
    #     print(login.user)  # 打印关联的详细信息（通过backref生成的user属性）

    # 示例2：通过详细信息查询登录用户
    with Session() as session:
        user = session.query(User).first()  # 获取第一个详细信息
        print(user.login_user)  # 打印关联的登录用户（通过login_user属性）


# 程序入口
if __name__ == '__main__':
    # 功能开关（取消注释对应行执行相应操作）
    # Base.metadata.create_all(bind=engine)  # 创建数据表（首次运行时需要）
    # add_date()  # 执行方式1添加数据
    # query_data()  # 执行查询
    # add_date2()  # 执行方式2添加数据
    query_data()