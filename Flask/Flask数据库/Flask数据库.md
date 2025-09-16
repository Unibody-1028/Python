## SQLAlchemy介绍

![image-20250908233432759](assets/image-20250908233432759.png)

SQLAlchemy是一个ORM框架

​	**对象关系映射(Object Relational Mapping,简称ORM)**,是一种程序设计技术,用于实现面向对象编程语言里不同类型系统的数据之间的转换.从效果上看,它其实是建立了一个可以在编程语言里使用的"虚拟对象数据库",即对象模型与数据库表的映射

**为什么要有SQLAlchemy**

随着项目的越来越大,编写原生SQL的方式会在代码中出现大量重复的语句,存在以下问题:

1. SQL语句重复利用率低,越复杂的SQL语句条件越多,代码越长,会出现很多相似的SQL语句
2. 很多SQL语句是在业务逻辑中拼接出来的,如果数据库需要修改,就需要去修改这些逻辑,可能会遗漏对SQL语句的修改
3. SQL容易出现web安全问题



​	ORM可以通过类的方式去操作数据库而不需要编写原生的SQL语句,ORM会把表映射成类,把行映射为实例,把字段映射为属性,但在执行对象操作时最终还是会把对象的操作转换为数据库的原生语句,ORM有以下优点:

1. 易用性:使用ORM做数据库开发可以有效减少重复的SQL语句,写出的模型也会更加直观、清晰
2. 性能损耗小:虽然ORM转换成底层数据库操作指令存在一些开销,但只要不是对性能有严苛的要求,使用ORM可以大大提高开发效率并提高代码可读性
3. 设计灵活:使用ORM可以轻松卸除复杂的查询
4. 可移植性强:SQLAlchemy封装了底层的数据库实现,支持多个关系数据库,包括流行的Mysql、PostgreSQ和SQLite,可以轻松的切换数据库





## SQLAlchemy操作数据库

![image-20250909002613722](assets/image-20250909002613722.png) 

```python
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

```



## ORM模型映射到数据库中

![image-20250909005920845](assets/image-20250909005920845.png) 



```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base  # 关键修改：从sqlalchemy.orm导入
from sqlalchemy.orm import sessionmaker

# 数据库连接配置
HOST = 'localhost'
PORT = 3306
DATA_BASE = 'test'
USER = 'root'
PWD = '123456'

DB_URI = f'mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DATA_BASE}?charset=utf8mb4'
engine = create_engine(DB_URI)

# 创建基类（使用新路径的declarative_base）
Base = declarative_base()  # 此处不再需要传入engine，2.0版本已简化

class Person(Base):
    __tablename__ = 't_person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)  # 增加非空约束
    age = Column(Integer, default=0)
    country = Column(String(32))

    def __repr__(self):
        return f"<Person(id={self.id}, name='{self.name}')>"

# 创建数据表（需传入engine）
Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    # 测试添加数据
    try:
        session.add(Person(name='李四', age=30, country='中国'))
        session.commit()
        print("数据添加成功")
    except Exception as e:
        session.rollback()
        print(f"错误：{e}")
    finally:
        session.close()

```



## SQLAlchemy对数据的增删改查操作

![image-20250909011547922](assets/image-20250909011547922.png) 

```python
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# 数据库设置
HOST = 'localhost'
PORT = 3306
DATA_BASE = 'test'
USER = 'root'
PWD = '123456'

DB_URI = f'mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DATA_BASE}'

engine = create_engine(DB_URI)
Base = declarative_base()

class Person(Base):
    __tablename__ = 't_person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)
    country = Column(String(32))

# 创建数据表
# Base.metadata.create_all(engine)

# 创建会话对象来操作数据
session1 = sessionmaker(bind=engine)


def create_data():
    with session1() as session:
        session.add(Person(name='李四',age=30,country='中国'))
        p1 = Person(name='job',age=20,country='us')
        session.add(p1)
        # session.add_all([p1,p2,p3......])
        session.commit()
        print('数据添加成功')

def query_data_all():
    with session1() as session:
        all_person = session.query(Person).all()
        for p in all_person:
            print(f'{p.id}--{p.name}--{p.age}--{p.country}')

def query_data_by_params():
    with session1() as session:
        #p = session.query(Person).filter_by(name='job').first() # .all()
        p = session.query(Person).filter(Person.name=='job').first() # .all()
        print(f'{p.id}--{p.name}--{p.age}--{p.country}')

def update_data():
    with session1() as session:
        p = session.query(Person).filter(Person.name == 'job').first()
        p.age = 22
        session.commit()
        print(f'{p.id}--{p.name}--{p.age}--{p.country}')

def delete_data():
    with session1() as session:
        p = session.query(Person).filter(Person.name == 'job').first()
        session.delete(p)
        session.commit()


def delete_all_data():
    with session1() as session:
        p = session.query(Person).all()
        for p1 in p:
            session.delete(p1)
        session.commit()


if __name__ == '__main__':
    #create_data()
    query_data_all()
    #query_data_by_params()
    #update_data()
    #delete_data()
    #delete_all_data()
```



## SQLAlchemy常用数据类型

![image-20250909091620752](assets/image-20250909091620752.png) 

### 一、基础数据类型（最常用）

对应数据库中的基本字段类型，适用于存储简单值：

| SQLAlchemy 类型             | 数据库对应类型（以 MySQL 为例） | 说明及使用场景                                               | 示例代码                                                     |
| --------------------------- | ------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `Integer`                   | INT                             | 整数类型，用于存储整数（如 ID、年龄、数量），支持自增（`autoincrement=True`）。 | `id = Column(Integer, primary_key=True, autoincrement=True)` |
| `String(length)`            | VARCHAR(length)                 | 字符串类型，需指定长度（如 32、64），用于存储短文本（用户名、标题、地址）。 | `name = Column(String(32), nullable=False)`                  |
| `Text`                      | TEXT                            | 长文本类型，无需指定长度，用于存储大量文本（文章内容、备注、日志）。 | `content = Column(Text)`                                     |
| `Float`                     | FLOAT/DOUBLE                    | 浮点类型，用于存储小数（如价格、权重、评分），精度有限。     | `price = Column(Float, default=0.0)`                         |
| `Numeric(precision, scale)` | DECIMAL(precision, scale)       | 高精度小数类型，`precision` 总位数，`scale` 小数位数（如金额、税率，避免浮点误差）。 | `balance = Column(Numeric(10, 2))` # 最大 9999999.99         |
| `Boolean`                   | TINYINT(1)                      | 布尔类型，存储 `True`（1）或 `False`（0），用于表示状态（是否激活、是否删除）。 | `is_active = Column(Boolean, default=True)`                  |
| `DateTime`                  | DATETIME                        | 日期时间类型，存储具体时间（如创建时间、登录时间），需配合 `datetime` 模块使用。 | `create_time = Column(DateTime, default=datetime.datetime.now)` |
| `Date`                      | DATE                            | 日期类型，仅存储年月日（如生日、到期日）。                   | `birthday = Column(Date)`                                    |
| `Time`                      | TIME                            | 时间类型，仅存储时分秒（如每日打卡时间）。                   | `checkin_time = Column(Time)`                                |

### 二、特殊数据类型（场景化需求）

适用于特定格式或复杂结构的数据：

| SQLAlchemy 类型 | 说明及使用场景                                               | 示例代码                                                     |
| --------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `Enum(*values)` | 枚举类型，限制字段值只能是预定义的选项（如性别、订单状态），避免无效值。 | `gender = Column(Enum('male', 'female', 'other'), default='other')` |
| `JSON`          | JSON 类型，存储 JSON 格式数据（如配置信息、嵌套结构数据），MySQL 5.7+ 支持。 | `config = Column(JSON, default={})` # 存储字典或列表         |
| `LargeBinary`   | 二进制类型，存储字节数据（如图片、文件内容，通常建议存路径而非文件本身）。 | `avatar = Column(LargeBinary)` # 不推荐，优先用 String 存图片路径 |
| `UUID`          | 通用唯一识别码，生成唯一字符串（如分布式系统中的唯一标识），需导入 `sqlalchemy.dialects.postgresql.UUID`。 | `uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)`      |

### 三、关系型类型（ORM 关联专用）

用于定义模型间的关系（如一对一、一对多、多对多），需结合 `relationship` 使用：

| 关系类型       | 说明                                                         | 示例场景                                                     |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `relationship` | 定义模型间的关联关系（非数据库字段，仅 ORM 层面的逻辑关联）。 | 一个用户（User）有多个订单（Order）： `orders = relationship('Order', backref='user')` |

### 四、类型选择原则

1. **匹配数据长度**：短文本用 `String`（指定长度），长文本用 `Text`；
2. **保证精度**：金额、税率等需精确计算的用 `Numeric`，避免 `Float` 的精度误差；
3. **节省空间**：根据实际需求选择最小合适类型（如年龄用 `Integer` 而非 `BigInteger`）；
4. **兼容数据库**：部分类型是特定数据库支持的（如 `JSON` 在 MySQL 5.7+ 可用），跨库开发需注意兼容性。

```python
import enum
from datetime import date, datetime, time

from sqlalchemy import create_engine, Column, Integer, String, Float, String, Boolean, Enum, Date, DateTime, Text, \
    DECIMAL, Time
from sqlalchemy.orm import sessionmaker, declarative_base

# 数据库设置
HOST = 'localhost'
PORT = 3306
DATA_BASE = 'test'
USER = 'root'
PWD = '123456'

DB_URI = f'mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DATA_BASE}'

engine = create_engine(DB_URI)
Base = declarative_base()
session1 = sessionmaker(engine)


class TagEnum(enum.Enum):
    Python = 'Python'
    JAVA = 'JAVA'


class News(Base):
    __tablename__ = 't_news'
    id = Column(Integer, autoincrement=True, primary_key=True)
    price1 = Column(Float)
    price2 = Column(DECIMAL)
    title = Column(String(32))
    is_delete = Column(Boolean)
    tag1 = Column(Enum('Python', 'JAVA'))
    tag2 = Column(Enum(TagEnum))
    create_time = Column(Date)
    update_time = Column(DateTime)
    delete_time = Column(Time)
    content = Column(Text)


def add_data():
    news1 = News(
        price1=1234.567890,
        price2=1234.567890,
        title='SQLAlchemy测试数据',
        is_delete=True,
        tag1='Python',
        tag2='JAVA',
        create_time=date(2020, 1, 1),
        update_time=datetime(2020, 2, 1, 0, 0, 0),
        delete_time=time(0, 0, 1),
        content='测试内容'
    )
    with session1() as session:
        session.add(news1)
        session.commit()
        print('数据添加成功')


if __name__ == '__main__':
    #Base.metadata.create_all(bind=engine)
    add_data()
```





## Column常用字段参数

![image-20250909103531775](assets/image-20250909103531775.png) 

### 一、核心必选参数(字段类型与主键)

| 参数           | 作用                                                         | 示例                                     |
| -------------- | ------------------------------------------------------------ | ---------------------------------------- |
| 第一个位置参数 | 指定字段数据类型（如 `Integer`、`String` 等），是唯一必填参数。 | `id = Column(Integer)`                   |
| `primary_key`  | 设为 `True` 表示该字段是主键（唯一标识记录），一个表通常有一个主键。 | `id = Column(Integer, primary_key=True)` |

### 二、约束类参数

| 参数             | 作用                                                         | 示例                                                         |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `nullable`       | 默认为 `True`（允许为空），设为 `False` 则强制字段必须有值（非空约束）。 | `name = Column(String(32), nullable=False)`                  |
| `unique`         | 设为 `True` 表示字段值在表中必须唯一（唯一约束），如用户名不能重复。 | `email = Column(String(64), unique=True)`                    |
| `index`          | 设为 `True` 为该字段创建索引（加速查询），适合频繁作为查询条件的字段。 | `phone = Column(String(11), index=True)`                     |
| `default`        | 设置字段默认值，插入数据时若未指定该字段，则使用默认值。     | `age = Column(Integer, default=0)`                           |
| `server_default` | 与 `default` 类似，但默认值由数据库服务器生成（而非客户端），更可靠。 | `create_time = Column(DateTime, server_default=func.now())`  |
| `autoincrement`  | 仅对整数主键有效，设为 `True` 表示自动增长（默认对主键生效）。 | `id = Column(Integer, primary_key=True, autoincrement=True)` |

### 三、描述与映射参数

| 参数      | 作用                                                         | 示例                                                   |                           |
| --------- | ------------------------------------------------------------ | ------------------------------------------------------ | ------------------------- |
| `comment` | 为字段添加注释（数据库层面可见），方便维护时理解字段含义。   | `country = Column(String(32), comment='用户所在国家')` |                           |
| `name`    | 指定字段在数据库中的实际列名（默认与模型类中字段名一致），用于解决命名冲突。 | `user_name = Column(String(32), name='username')`      | # 数据库中列名为 username |
| `type_`   | 显式指定字段类型（一般无需使用，直接将类型作为第一个参数即可）。 | `age = Column(type_=Integer)`                          |                           |

### 四、关系型数据库专用参数

| 参数                  | 作用                                                         | 适用场景                                                     |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `foreign_keys`        | 指定外键关联的字段，用于多表关联时约束数据引用完整性。       | `user_id = Column(Integer, foreign_keys=[User.id])`          |
| `onupdate`/`ondelete` | 设置外键更新 / 删除时的行为（如 `CASCADE` 级联操作），需配合外键使用。 | `user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))` |



```python
from requests import session
from sqlalchemy import Column, Integer, String, DateTime

from Flask.Flask数据库.db_util import engine
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


```



## SQLAlchemy中query函数的使用

![image-20250909143655243](assets/image-20250909143655243.png) 

**`query()`方法由会话(Session)对象调用,最基础的用法是指定要查询的模型类或字段,返回一个查询对象,再通过后续方法获取结果**

### query查询

1. 查询整个模型

    ```python
    # 查询Person表的所有记录(返回Person实例的列表)
    all_Person = session.query(Person).all()
    for person in all_Person:
        print(person.name,person.age,...) # 访问实例属性
    ```

2. 查询指定字段

    ```python
    # 查询name和age字段,返回(name,age)元组的列表
    name_age_list = session.query(Persom.name,Person.age).all()
    for name,age in name_age_list:
        print(f"姓名:{name},年龄:{age}"
    ```

### 结果处理方法

查询对象需要通过以下方法获取最终结果：

| 方法       | 作用                                  | 示例                                                         |
| ---------- | ------------------------------------- | ------------------------------------------------------------ |
| `all()`    | 返回所有符合条件的结果（列表）        | `session.query(Person).all()`                                |
| `first()`  | 返回第一条结果（无结果则返回 None）   | `session.query(Person).first()`                              |
| `one()`    | 返回唯一结果（结果数量不为 1 则报错） | `session.query(Person).filter_by(id=1).one()`                |
| `scalar()` | 返回单值结果（适合聚合查询）          | `session.query(Person.age).filter_by(id=1).scalar()`         |
| `count()`  | 返回结果数量                          | `session.query(Person).filter(Person.country == '中国').count()` |

### 高级用法

#### 1. 排序（`order_by()`）

```python
# 按年龄升序（默认）
sorted_by_age = session.query(Person).order_by(Person.age).all()
# 按年龄降序（加 desc()）
sorted_by_age_desc = session.query(Person).order_by(Person.age.desc()).all()
```

#### 2. 限制结果数量（`limit()` 和 `offset()`）

```python
# 只取前 10 条
top10 = session.query(Person).limit(10).all()
# 跳过前 5 条，取接下来的 10 条（分页常用）
page2 = session.query(Person).offset(5).limit(10).all()
```

#### 3. 聚合查询（结合 `func`）

```python
from sqlalchemy import func

# 计算平均年龄
avg_age = session.query(func.avg(Person.age)).scalar()
# 统计每个国家的人数
country_count = session.query(
    Person.country, 
    func.count(Person.id)  # 按国家分组计数
).group_by(Person.country).all()
```





## filter过滤数据

![image-20250909165301653](assets/image-20250909165301653.png) 

**使用过滤条件查询**

1. `filter_by():`简单条件查询(关键字参数),适合单表查询,参数是"字段名=值"的关键字形式

    ```python
    # 查询age=25的记录
    person = session.query(Person).filter_by(age=25).all()
    ```

2. `filter():`支持复杂条件查询,参数是"模型.字段 运算符 值"的形式:

    **1.比较条件**

    ```python
    # 年龄 > 30 
    adults = session.query(Person).filter(Person.age>30).all()
    # 查询姓名不是张三的所有人
    not_zhang = session.query(Person).filter(Person.name!='张三').all()
    # 查询年龄在18-30之间的所有人
    young_people = session.quety(Person).filter(Person.age.between(18,30)).all()
    ```

    **2.逻辑条件(AND/OR)**

    ```python
    from sqlalchemy import and_,or_ # 导入逻辑运算符
    ```

    ```python
    # 中国且年龄>25
    chinese_and_age_over_25 = session.query(Person).filter(
    	and_(Person.country == '中国',Person.age > 25)
    ).all()
    
    # 年龄<18或国家为美国
    young_or_us = session.query(Person).filter(
    	or_(Person.age<18,Person.country=='美国')
    ).all()
    ```

    **3.模糊查询(like)**

    ```python
    # 姓名以张开头
    zhang_family = session.query(Person).filter(Person.name.like('张%')).all()
    ```

    



## 表关系

![image-20250909182039374](assets/image-20250909182039374.png) 

表之间的关系存在三种:一对一、一对多、多对多,SQLAlchemy中的ORM也可以模拟这三种关系,一对一关系在SQLAlchemy中是通过一对多的关系模拟的

**外键:**

​	使用SQLAlchemy创建外键只需要在从表中增加一个字段,指定这个字段外键的是哪个表的字段就可以,从表中外键的字段, 必须和主表的主键字段类型保持一致.

```python
# 主表/从表
# user/news

from sqlalchemy import Column, Integer, String, Text, ForeignKey

from db_util import Base



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    uname = Column(String(50),nullable=False)

    def __repr__(self):
        return f'<User(uname:{self.uname})>'

class News(Base):
    __tablename__ = 'news'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    content = Column(Text,nullable=False)
    uid = Column(Integer,ForeignKey('user.id'))

    def __repr__(self):
        return f'<News(title:{self.title}, content:{self.content})>'


```

**外键约束有以下几项:**

- `RESTRICT:`若子表中有父表对应的关联数据,删除父表对应的数据,会阻止删除.默认设置
- `NO ACTION:`在`MYSQL`中,同`RESTRICT`
- `CASCADE:`级联删除
- `SET NULL:`父表对应数据被删除,子表对应的数据项会设置为`NULL`



## ORM关系-一对多

![image-20250910155400600](assets/image-20250910155400600.png) 

​	SQLAlchemy提供了一个`relationship`,这个类可以定义属性,以后在访问相关联的表的时候就可以直接通过属性访问的方式使用.另外,可以通过`backref`来指定反向访问的属性名称

```python
# 导入所需模块
from requests import session  
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
```

## ORM关系-一对一

![image-20250910171552975](assets/image-20250910171552975.png) 

```python
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
```

## ORM关系-多对多

![image-20250910180027641](assets/image-20250910180027641.png) 

- 多对多的关系需要通过一张中间表来绑定他们之间的关系
- 先把两个需要做多对多的模型定义出来
- 使用Table定义一个中间表,中间表一般包含两个模型的外键,并且让他们两个作为一个"复合主键"
- 在两个需要做多对多的模型中随便选择一个模型,定义一个`relationship`属性,来绑定三者之间的关系,在使用`relationship`时,需要传入一个`secondary`=中间表对象名

```python
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from Flask.Flask数据库.db_util import engine  # 自定义数据库引擎
from db_util import Base, Session  # 自定义模型基类和会话工厂

# 1. 定义多对多关系的中间表（必须在两个关联模型之前定义）
# 中间表用于关联 News（新闻表）和 Tag（标签表），无实体类，仅用 Table 定义结构
news_tag = Table(
    't_news_tag',  # 中间表的数据库表名
    Base.metadata,  # 关联到模型基类的元数据（用于创建表）

    # 字段1：关联新闻表的外键（主键之一）
    Column(
        'news_id',  # 中间表字段名
        Integer,
        ForeignKey('t_news_n_n.id'),  # 关联新闻表 t_news_n_n 的主键 id
        primary_key=True  # 中间表用复合主键（news_id + tag_id）确保唯一性
    ),

    # 字段2：关联标签表的外键（主键之一）- 修复原代码的关联错误
    Column(
        'tag_id',  # 中间表字段名
        Integer,
        ForeignKey('t_tags_n_n.id'),  # 正确关联标签表 t_tags_n_n 的主键 id（原代码错关联到新闻表）
        primary_key=True
    )
)


# 2. 定义新闻模型（主模型1）
class News(Base):
    __tablename__ = 't_news_n_n'  # 新闻表的数据库表名

    id = Column(Integer, primary_key=True, autoincrement=True)  # 主键自增
    title = Column(String(32), nullable=False)  # 新闻标题（非空）

    # 定义与 Tag 的多对多关系
    tags = relationship(
        'Tag',  # 关联的目标模型（标签表）
        backref='news',  # 在 Tag 模型中自动生成 'news' 属性，用于反向查询关联的新闻
        secondary=news_tag  # 关键：传入中间表对象（而非字符串），建立多对多关联
    )

    # 自定义实例打印格式（方便调试）
    def __repr__(self):
        return f'<News: id={self.id} title={self.title}>'


# 3. 定义标签模型（主模型2）
class Tag(Base):
    __tablename__ = 't_tags_n_n'  # 标签表的数据库表名

    id = Column(Integer, primary_key=True, autoincrement=True)  # 主键自增
    name = Column(String(32), nullable=False)  # 标签名称（非空）

    # 自定义实例打印格式（修复原代码的字段名错误：title 改为 name）
    def __repr__(self):
        return f'<Tag: id={self.id} name={self.name}>'  # 原代码误写为 title={self.name}


# 4. 向数据库添加多对多关联数据
def add_data():
    # 创建两个新闻实例
    news1 = News(title='Python 教程')
    news2 = News(title='JAVA 实战')

    # 创建两个标签实例
    tag1 = Tag(name='IT')
    tag2 = Tag(name='科技')

    # 建立多对多关联：给新闻添加标签（通过 relationship 生成的 tags 列表）
    news1.tags.append(tag1)  # Python 教程 → IT
    news1.tags.append(tag2)  # Python 教程 → 科技
    news2.tags.append(tag1)  # JAVA 实战 → IT
    news2.tags.append(tag2)  # JAVA 实战 → 科技

    # 保存数据到数据库（with 语句自动管理会话生命周期，避免资源泄露）
    with Session() as session:
        session.add(news1)  # 添加新闻1（关联的标签会自动保存）
        session.add(news2)  # 添加新闻2（关联的标签会自动保存）
        session.commit()  # 提交事务
    print("多对多数据添加成功！")

def query_data():
    with Session() as session:
        news = session.query(News).first()
        print(news.tags)


# 5. 程序入口
if __name__ == '__main__':
    # 首次运行时取消注释，创建所有表（包括中间表 t_news_tag）
    # Base.metadata.create_all(bind=engine)

    # 执行添加数据操作
    #add_data()
    query_data()
```



## ORM删除数据注意事项

![image-20250911095805990](assets/image-20250911095805990.png) 

​	**ORM删除数据,会无视mysql级别的外键约束,会直接将对应的数据删除,然后将表中的那个外键设置为NULL,也就是数据库的`SET NULL`.如果想要避免这种行为,应该设置表中外键的`nullable=False`**

```python
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
```



## ORM中relationship方法中的cascade参数

![image-20250911103534644](assets/image-20250911103534644.png) 

​	在SQLAlchemy中,只要将一个数据添加到session中,提交该数据时,其它相关联的数据会自动存入到数据库,这个行为是通过参数`cascade`控制的.

**cascade参数:**

`save-update:`默认选项,在添加一条数据时,会把其它的关联数据都添加到数据库中

`delete:`控制删除某个模型中数据时,是否选择删除使用`relationship`与它相关联的数据

`delete-orphan:`当一个ORM对象解除了父表中的关联对象时,自己便会被删除掉,如果父表中的数据被删除,自己也会被删除,这个选项只能用在一对多关系上,并且还需要在子模型的`relationship`中,增加一个`single_parent=True`的选项

`merge:`默认选项,使用`session.merge`,合并一个对象时,会将使用了`relationship`相关联的对象也进行`merge`操作

`expunge:`进行移除操作时,也会将相关联的对象进行移除,这个操作只是从session中移除,并不会从数据库中移除

`all:`上面几种行为的缩写



```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref  # backref用于显式定义反向关联

# 导入自定义数据库工具：引擎（连接数据库）、基类（所有模型的父类）、会话工厂（操作数据）
from Flask.Flask数据库.db_util import engine
from db_util import Base, Session


# 主表：用户表（一对多关系中的“一”方）
class User(Base):
    __tablename__ = 't_user'  # 数据库中实际表名
    id = Column(Integer, primary_key=True, autoincrement=True)  # 主键自增
    name = Column(String(32))  # 用户名

    # ------------------------------ 以下是不同cascade配置的注释说明 ------------------------------
    # 1. cascade=''：完全关闭所有级联操作
    # articles = relationship('Article', backref='user', cascade='')
    # 效果：主表（User）的增/删/改操作，完全不影响子表（Article）
    # - 新增User时，关联的Article不会自动保存（需手动add(Article)）
    # - 删除User时，关联的Article不会被删除（可能产生“孤儿记录”）
    # - 更新User时，关联的Article不会同步更新


    # 2. cascade='save-update'：仅开启“保存/更新”级联（默认配置含此选项，还包含merge）
    # articles = relationship('Article', backref='user', cascade='save-update')
    # 效果：主表的“保存/更新”操作会级联到子表
    # - 新增User并关联Article时，add(User)会自动保存关联的Article（无需手动add(Article)）
    # - 删除User时，关联的Article不会被删除（需配合其他配置实现级联删除）
    # - 默认值实际是 'save-update, merge'，merge用于“合并离线数据”时级联处理子表


    # 3. cascade='save-update, delete'：开启“保存/更新 + 级联删除”
    # articles = relationship('Article', backref='user', cascade='save-update, delete')
    # 效果：在“保存/更新”基础上，增加“删除主表时自动删除子表”
    # - 删除User时，所有关联的Article会被自动删除（避免孤儿记录）
    # - 注意：此配置仅在“通过主表删除”时生效（如delete(User)），直接删除子表（delete(Article)）不影响主表


    # 4. cascade='save-update, delete, delete-orphan' + single_parent=True：级联删除“孤儿子表”
    # articles = relationship('Article', backref='user', cascade='save-update,delete,delete-orphan', single_parent=True)
    # 关键效果解析：
    # - delete-orphan：当子表与主表的关联被解除（如user.articles = []清空关联），该子表会被自动删除
    # - single_parent=True：强制子表必须属于一个主表（防止手动解除关联后子表成为孤儿，是delete-orphan的必要搭配）
    # 场景：适合“文章必须属于某个用户”，若解除用户与文章的关联，文章需被删除


# 从表：文章表（一对多关系中的“多”方，一个用户可有多篇文章）
class Article(Base):
    __tablename__ = 't_article'  # 数据库中实际表名
    id = Column(Integer, primary_key=True, autoincrement=True)  # 主键自增
    title = Column(String(32))  # 文章标题
    uid = Column(Integer, ForeignKey('t_user.id'))  # 外键：关联用户表的id字段

    # ------------------------------ 核心关联配置：backref显式定义反向关联 ------------------------------
    # 此处将关联关系的“级联规则”定义在反向关联（User.articles）中，而非正向关联（Article.user）
    # 等价于：在User类中定义 articles = relationship('Article', cascade='save-update,delete')，同时在Article中生成user属性
    user = relationship(
        'User',  # 关联的目标主表模型（User）
        backref=backref(  # 显式创建反向关联属性
            'articles',  # 反向关联的属性名：User类会自动生成articles属性，用于访问所有关联的Article
            cascade='save-update,delete'  # 级联规则：绑定到User.articles，控制主表操作对子表的影响
        )
    )

    # 原有注释补充：
    # - 正向关联：Article实例通过user属性访问所属的User实例（如 art1.user → 对应的用户）
    # - 反向关联：User实例通过articles属性访问所有关联的Article实例（如 user1.articles → [art1, art2]）
    # - 级联规则作用：此处cascade='save-update,delete'意味着：
    #   1. 新增User并关联Article时，add(User)会自动保存Article
    #   2. 删除User时，会自动删除所有关联的Article


# ------------------------------ 数据操作函数注释 ------------------------------
def add_data():
    # 1. 先删除所有表（重置数据，避免重复创建），再重新创建表结构
    Base.metadata.drop_all(bind=engine)  # 删除所有模型对应的表
    Base.metadata.create_all(bind=engine)  # 根据模型创建表（含外键约束）

    # 2. 初始化数据：创建1个用户和2篇关联文章
    user = User(name='SXT')  # 创建用户实例
    art1 = Article(title='Python教程', uid=1)  # 创建文章1，uid=1（关联用户id=1）
    art2 = Article(title='JAVA实战', uid=1)  # 创建文章2，uid=1（关联同一用户）

    # 3. 建立ORM层面的关联：将文章添加到用户的articles列表
    user.articles.append(art1)
    user.articles.append(art2)

    # 4. 保存数据到数据库
    with Session() as session:  # 用with语句自动管理会话（结束后自动关闭，避免资源泄露）
        session.add(user)  # 仅添加用户实例（因cascade='save-update'，关联的文章会自动保存）
        session.commit()  # 提交事务（实际写入数据库）
    print("数据初始化完成：1个用户 + 2篇文章")


def delete_data():
    # 功能：删除主表（User）数据，验证级联删除效果
    with Session() as session:
        # 查询第一个用户（即add_data中创建的SXT）
        user = session.query(User).first()
        if user:
            session.delete(user)  # 删除用户（因cascade='delete'，关联的2篇文章会被自动删除）
            session.commit()  # 提交事务
            print(f"已删除用户：{user.name}，及其关联的所有文章")
        else:
            print("未找到可删除的用户")


def delete_art():
    # 功能：直接删除子表（Article）数据，验证主表是否受影响
    with Session() as session:
        # 查询第一篇文章
        art = session.query(Article).first()
        if art:
            session.delete(art)  # 直接删除文章（级联规则仅影响“主表删子表”，子表删主表无影响）
            session.commit()  # 提交事务
            print(f"已删除文章：{art.title}，关联的用户不受影响")
        else:
            print("未找到可删除的文章")


def update_data():
    # 功能：解除用户与文章的关联，验证是否触发“孤儿删除”（需配合cascade='delete-orphan'）
    with Session() as session:
        user = session.query(User).first()
        if user:
            # 将用户的articles列表清空（解除所有文章的关联）
            user.articles = []
            session.commit()  # 提交事务
            # 效果取决于cascade配置：
            # - 若有delete-orphan：清空后关联的文章会被自动删除
            # - 若无delete-orphan：文章仍存在，但uid与用户id的关联断裂（成为孤儿记录）
            print(f"已清空用户 {user.name} 的所有文章关联")
        else:
            print("未找到可操作的用户")


# ------------------------------ 程序入口：执行指定函数 ------------------------------
if __name__ == '__main__':
    add_data()  # 第一步：初始化数据（创建用户和文章）
    # delete_data()  # 第二步（可选）：删除用户，验证级联删除文章
    # update_data()  # 第二步（可选）：清空用户的文章关联，验证孤儿删除
    # delete_art()   # 第二步（可选）：直接删除文章，验证主表不受影响
```



## ORM中的排序

![image-20250911130406095](assets/image-20250911130406095.png) 

**order_by:**可以根据模型中某个属性进行排序,"模型名.属性名.desc()"表示降序排序

```python
# 导入随机整数生成模块：用于生成随机年龄、随机新闻数量、随机阅读量
from random import randint

# 导入SQLAlchemy核心组件：字段类型（Column/Integer等）、外键（ForeignKey）、关系定义工具（relationship/backref）
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

# 导入自定义数据库工具：
# - engine：数据库连接引擎（负责与数据库建立连接）
# - Session：会话工厂（创建操作数据库的会话，类似“数据库操作手柄”）
# - Base：所有模型类的父类（统一管理表结构）
from Flask.Flask数据库.db_util import engine
from db_util import Session, Base


# 主表：用户模型（一对多关系中的“一”方）
# 一个用户可以拥有多篇新闻，通过反向关联属性`news`访问
class User(Base):
    __tablename__ = 't_user'  # 数据库中实际的表名（避免与其他表重名）
    # 主键字段：自增整数，唯一标识每个用户（数据库层面确保唯一性）
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 用户名：字符串类型（长度32），存储用户名称
    name = Column(String(32))
    # 用户年龄：整数类型，存储用户年龄
    age = Column(Integer)

    # 自定义实例打印格式（调试时直接打印用户对象，会显示此格式，便于查看信息）
    def __repr__(self):
        return f'<User: id={self.id} name={self.name} age={self.age}>'


# 从表：新闻模型（一对多关系中的“多”方）
# 多篇新闻归属同一个用户，通过外键`uid`关联用户表，通过`user`属性访问所属用户
class News(Base):
    __tablename__ = 't_news'  # 数据库中实际的表名
    # 主键字段：自增整数，唯一标识每篇新闻
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 新闻标题：字符串类型（长度32），非空约束（数据库层面强制必须填写，不能为NULL）
    title = Column(String(32), nullable=False)
    # 新闻内容：字符串类型（长度32），非空约束（同上，确保内容不缺失）
    content = Column(String(32), nullable=False)
    # 新闻阅读量：整数类型，存储新闻被查看的次数
    read_count = Column(Integer)

    # 外键字段：关联用户表（t_user）的主键（id）
    # 作用：数据库层面建立“新闻-用户”的关联，确保新闻必须归属一个已存在的用户（除非允许NULL）
    uid = Column(Integer, ForeignKey('t_user.id'))

    # ORM层面的关系定义：连接News与User模型
    user = relationship(
        'User',  # 关联的目标模型（即主表User）
        # backref：在目标模型（User）中自动生成反向关联属性
        # - 'news'：User类会新增`news`属性，通过`user.news`可获取该用户的所有新闻
        # - order_by=read_count.desc()：反向关联查询时，新闻默认按“阅读量（read_count）降序”排序
        #   （desc()表示降序，即阅读量高的新闻排在前面；asc()为升序，默认不写时为升序）
        backref=backref('news', order_by=read_count.desc())
    )

    # 自定义实例打印格式（调试时打印新闻对象，显示关键信息）
    def __repr__(self):
        return f'<News: id={self.id} uid={self.uid} title={self.title} content={self.content} read_count={self.read_count}>'


# 函数：批量添加测试数据（生成10个用户，每个用户对应1~8篇随机数量的新闻）
def add_data():
    # 使用with语句管理会话：
    # - 自动创建会话，代码块执行完后自动关闭会话（避免资源泄露，无需手动session.close()）
    # - 若代码块内报错，会话会自动回滚（确保数据一致性）
    with Session() as session:
        # 外层循环：生成10个用户（i从0到9，共10次）
        for i in range(10):
            # 1. 创建用户实例：
            # - name=f'name{i+1}'：用户名按“name1~name10”规律生成（i+1避免name0）
            # - age=randint(5,30)：年龄在5~30之间随机（闭区间，包含5和30）
            user = User(name=f'name{i+1}', age=randint(5, 30))
            # 将用户添加到会话：此时用户暂未写入数据库，仅在会话中暂存
            session.add(user)

            # 内层循环：为当前用户生成1~8篇随机数量的新闻
            # randint(1,8)：每次循环生成1到8之间的随机整数（即每个用户的新闻数不固定）
            for j in range(randint(1, 8)):
                # 2. 创建新闻实例：
                # - title=f'title{j+1}'：新闻标题按“title1~titleN”生成（N为当前用户的新闻数）
                # - content=f'info{j}'：新闻内容按“info0~infoN-1”生成（与标题序号对应）
                # - read_count=randint(1,100)：阅读量在1~100之间随机
                news = News(title=f'title{j+1}', content=f'info{j}', read_count=randint(1, 100))
                # 3. 建立用户与新闻的关联：
                # 通过User的反向关联属性`news`（列表）添加新闻，ORM会自动维护外键`uid`
                # 因SQLAlchemy默认cascade含“save-update”，添加用户时会自动保存关联的新闻（无需手动session.add(news)）
                user.news.append(news)

        # 提交事务：将会话中所有暂存的操作（10个用户+随机新闻）一次性写入数据库
        # 只有执行commit()，数据才会真正保存到数据库，否则所有操作会在会话关闭后丢弃
        session.commit()
    print("批量数据添加完成！生成10个用户，每个用户对应1~8篇新闻")


# 函数：查询所有用户，并按年龄降序排列（从大到小）
def query_user():
    with Session() as session:
        # 1. 查询User表所有记录：session.query(User).all()
        # 2. 按年龄降序排序：order_by(User.age.desc())
        #    - User.age：指定排序字段为用户年龄
        #    - desc()：降序排序（不写则默认升序asc()）
        users = session.query(User).order_by(User.age.desc()).all()
        
        # 遍历打印每个用户信息（调用User类的__repr__方法，格式清晰）
        print("\n所有用户（按年龄降序）：")
        for u in users:
            print(u)


# 函数：查询“最后一个用户”的所有新闻（默认按阅读量降序）
def query_news():
    with Session() as session:
        # 1. 查询所有用户：返回列表，顺序与数据库存储顺序一致（默认按主键id升序）
        users = session.query(User).all()
        
        # 2. 获取最后一个用户：users[-1]（Python列表负索引，-1表示最后一个元素）
        # 3. 通过用户的反向关联属性`news`获取该用户的所有新闻：
        #    - 新闻顺序由News.user的backref配置决定（order_by=read_count.desc()，即阅读量降序）
        last_user = users[-1]
        user_news = last_user.news
        
        # 遍历打印该用户的所有新闻（调用News类的__repr__方法）
        print(f"\n最后一个用户（{last_user.name}，id={last_user.id}）的新闻（按阅读量降序）：")
        for news in user_news:
            print(news)


# 程序入口：根据需求取消注释对应功能（首次运行需按“删表→建表→加数据”顺序执行）
if __name__ == '__main__':
    # 1. 首次运行前执行：删除所有旧表（重置表结构，避免旧数据干扰）
    # Base.metadata.drop_all(engine)
    
    # 2. 首次运行前执行：根据模型类创建新表（含外键约束、非空约束等）
    # Base.metadata.create_all(engine)
    
    # 3. 执行数据添加：生成10个用户+随机新闻
    # add_data()
    
    # 4. 执行用户查询：查看所有用户（按年龄降序）
    # query_user()
    
    # 5. 执行新闻查询：查看最后一个用户的新闻（按阅读量降序）
    query_news()
    

    
'''
嵌套循环生成数据的逻辑：
明确外层循环（生成 10 个固定用户）与内层循环（每个用户生成 1~8 篇随机新闻）的分工，解释 randint(1,8) 如何实现 “新闻数量随机”，以及 j 索引如何避免同一用户的新闻标题重复。
backref 排序的实际效果：
强调 order_by=read_count.desc() 是 “反向关联的默认排序”—— 无需在 query_news 中额外写排序代码，last_user.news 直接返回按阅读量降序的新闻列表，体现 ORM 配置的便捷性。
会话与事务的细节：
解释 with Session() 的自动管理机制（无需手动关闭）、session.add(user) 为何能同时保存关联新闻（依赖默认 cascade='save-update'）、session.commit() 的关键作用（数据真正写入数据库）。
新手友好的操作引导：
在 __main__ 中标注 “首次运行顺序”（删表→建表→加数据），避免因操作顺序错误导致的报错（如未建表就加数据、旧表结构与新模型不匹配）。
'''
```



## SQLAlchemy数据的分页

![image-20250911134549941](assets/image-20250911134549941.png)

​	分页的核心需求是==避免一次性查询所有数据(防止内存溢出),只获取当前页的指定数量数据.==



| 工具         | ORM 层面定义                                                 | 对应的 SQL 语句                           | 核心作用                            |
| ------------ | ------------------------------------------------------------ | ----------------------------------------- | ----------------------------------- |
| `limit(n)`   | 限制查询结果的**最大条数**，即最多返回 `n` 条数据            | `SELECT ... FROM 表 LIMIT n`              | 控制 “每页显示多少条”（页大小）     |
| `offset(m)`  | 跳过查询结果的**前 m 条数据**，从第 `m+1` 条开始返回         | `SELECT ... FROM 表 OFFSET m`             | 控制 “从哪一页开始”（跳过前几页）   |
| `slice(a,b)` | 切片查询，返回结果中**从索引 a 到 b-1 的数据**（左闭右开），等价于 `offset(a).limit(b-a)` | `SELECT ... FROM 表 OFFSET a LIMIT (b-a)` | 一次性指定 “跳过条数” 和 “取数条数” |

```python
from random import randint

from sqlalchemy import Column, Integer, String

from Flask.Flask数据库.db_util import Base, Session, engine


class News(Base):
    __tablename__ = 't_news'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(32),nullable=False)
    content = Column(String(32),nullable=False)
    read_count = Column(Integer)

    def __repr__(self):
        return f'<User: id={self.id} title={self.title} content={self.content} read_count={self.read_count}>'

def add_data():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session() as session:
        for i in range(1,11):
            news = News(title=f'title{i}',content=f'info{i}',read_count=randint(1,1000))
            session.add(news)
        session.commit()

def query_by_limit():
    with Session() as session:
        news = session.query(News).limit(3).all()
        for n in news:
            print(n)

def query_by_offset():
    with Session() as session:
        news = session.query(News).offset(5).all()
        for n in news:
            print(n)

def query_by_slice():
    with Session() as session:
        news = session.query(News).slice(5,11).all()
        for n in news:
            print(n)
 

if __name__ == '__main__':
    # add_data()
    # query_by_limit()
    # query_by_offset()
    query_by_slice()
```



## SQLAlchemy数据懒加载

![image-20250911175432283](assets/image-20250911175432283.png) 

​	在SQLAlchemy ORM中,**数据懒加载(Lazy Loading)**是一种优化机制:当查询主表数据时,不会立即加载关联表的数据,而是在**首次访问关联数据时才触发实际查询**,这种按需加载的方式可以减少不必要的数据库交互,提升性能.

### 一、核心原理

假设存在 `User`（用户）和 `Article`（文章）的一对多关系（一个用户有多篇文章）：

```python
class User(Base):
    __tablename__ = 't_user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    # 关联文章，默认开启懒加载
    articles = relationship('Article', backref='user')

class Article(Base):
    __tablename__ = 't_article'
    id = Column(Integer, primary_key=True)
    title = Column(String(32))
    uid = Column(Integer, ForeignKey('t_user.id'))
```

- **非懒加载**：查询用户时，会立即执行 `JOIN` 语句，一次性加载用户及其所有文章（可能返回大量冗余数据）。
- **懒加载**：查询用户时，只加载用户本身的数据；**当首次访问 `user.articles` 时**，才会单独执行查询文章的 SQL（按需加载）。

### 二、懒加载的默认行为

SQLAlchemy 中，`relationship` 的 `lazy` 参数控制加载方式，**默认值为 `lazy='select'`（即懒加载）**，具体表现为：

1. **查询主表时只加载主表数据**：

    ```python
    with Session() as session:
        # 只执行查询用户的SQL：SELECT * FROM t_user WHERE id=1
        user = session.query(User).get(1)
        print(user.name)  # 此时未加载文章，无额外SQL
    ```

2. **首次访问关联数据时触发查询**：

    ```python
    # 首次访问 user.articles，触发查询文章的SQL：
    # SELECT * FROM t_article WHERE uid=1
    articles = user.articles  
    print(articles)  # 打印文章列表
    ```

3. **后续访问关联数据不会重复查询**：

    ```python
    # 第二次访问，直接使用已加载的缓存数据，不执行SQL
    print(user.articles)  
    ```

### 三、`lazy` 参数的可选值（加载策略）

除了默认的懒加载，`relationship` 还支持多种加载策略，通过 `lazy` 参数配置：

| `lazy` 值    | 加载方式说明                                                 | 适用场景                                                   |
| ------------ | ------------------------------------------------------------ | ---------------------------------------------------------- |
| `'select'`   | 默认值，懒加载：首次访问关联数据时执行单独查询               | 关联数据大、不常访问的场景（如用户的历史订单）             |
| `'joined'`   | 预加载：查询主表时通过 `JOIN` 一次性加载关联数据（非懒加载） | 关联数据小、必访问的场景（如文章和作者信息）               |
| `'subquery'` | 预加载：通过子查询一次性加载所有关联数据（非懒加载）         | 多对多关系或需要批量加载关联数据的场景                     |
| `'dynamic'`  | 动态懒加载：返回查询对象而非数据列表，可继续添加过滤条件（仅用于一对多 / 多对多） | 需要对关联数据分页、过滤的场景（如查询用户的前 10 篇文章） |

#### 1. `lazy='joined'`（预加载，非懒加载）

查询主表时通过 `JOIN` 加载关联数据，适合 “主表 + 关联表数据必用” 的场景：

```python
class User(Base):
    # ... 其他字段
    # 配置为预加载，查询用户时同时加载文章
    articles = relationship('Article', backref='user', lazy='joined')

# 使用时：
with Session() as session:
    # 执行一条JOIN查询：SELECT * FROM t_user JOIN t_article ON ...
    user = session.query(User).get(1)
    # 直接使用已加载的文章，无额外SQL
    print(user.articles)  
```

#### 2. `lazy='dynamic'`（动态懒加载，返回查询对象）

关联数据返回的是 `Query` 对象，可继续添加过滤、分页等条件，适合 “关联数据量大，需二次筛选” 的场景：

```python
class User(Base):
    # ... 其他字段
    # 动态懒加载，返回查询对象
    articles = relationship('Article', backref='user', lazy='dynamic')

# 使用时：
with Session() as session:
    user = session.query(User).get(1)
    # user.articles 是 Query 对象，可继续添加条件
    recent_articles = user.articles.order_by(Article.create_time.desc()).limit(10).all()
    print(recent_articles)  # 只查询用户的最近10篇文章
```

### 四、懒加载的优缺点

**优点：**

- **减少不必要的查询**：只加载实际需要的数据，避免一次性加载大量关联数据（尤其关联表数据量大时）。
- **简化代码**：无需手动编写复杂的 `JOIN` 语句，按需访问即可。

**缺点：**

- N+1 查询问题

    ：如果循环访问多个主表对象的关联数据，会触发 N+1 次查询（1 次查主表，N 次查每个主表的关联数据）。

    例如：

    ```python
    # 1次查询获取10个用户（N=10）
    users = session.query(User).limit(10).all()
    for user in users:
        # 每个用户触发1次查询，共10次 → 总11次查询
        print(user.articles)  
    ```

### 五、解决 N+1 查询问题：显式预加载

使用 `selectinload` 或 `joinedload` 强制预加载关联数据，避免 N+1 问题：

```python
from sqlalchemy.orm import selectinload

with Session() as session:
    # 显式预加载所有用户的文章，仅2次查询（1次用户，1次文章）
    users = session.query(User).options(selectinload(User.articles)).limit(10).all()
    for user in users:
        print(user.articles)  # 已预加载，无额外查询
```



==`lazy='dynamic'`只可以用在一对多和多对多关系,不可以用于一对一和多对一关系==



## 数据分组group_by和数据过滤分组having

![image-20250913014608369](assets/image-20250913014608369.png) 

### **group_by**

根据某个字段进行分组,例如想要根据年龄分组,来统计每个分组中有多少人

```python
r = session.query(User.age,func.count(User.id)).group_by(User.age).all()
```

### **having**

`having`是对分组查找结果进行二次过滤,例如想要查看未成年人的人数,就可以在年龄分组的基础上,对分组进行`having`过滤

```
r = session.query(User.age,func.count(User.id)).group_by(User.age).having(User.age<18).all()
```





## SQLAlchemy中Join的使用

![image-20250913021250173](assets/image-20250913021250173.png) 

​	在数据库查询中，**连接（JOIN）** 用于将两个或多个表基于共同的字段（通常是主键和外键）组合起来，获取关联数据。内连接、外连接（左连接、右连接、全外连接）是最常用的连接方式，核心区别在于**是否包含 “不匹配” 的数据行**，以及包含哪一侧表的不匹配数据。

### 一、核心概念

在理解具体连接前，先定义两个示例表，后续所有解释均基于这两个表：

- **表 A（用户表 users）**：存储用户基本信息，关键字段 `user_id`（主键）、`user_name`。
- **表 B（订单表 orders）**：存储用户订单信息，关键字段 `order_id`（主键）、`user_id`（外键，关联 users.user_id）、`order_amount`。

| users.user_id | users.user_name |
| ------------- | --------------- |
| 1             | 张三            |
| 2             | 李四            |
| 3             | 王五            |

| orders.order_id | orders.user_id | orders.order_amount |
| --------------- | -------------- | ------------------- |
| 101             | 1              | 100                 |
| 102             | 1              | 200                 |
| 103             | 2              | 150                 |

### 二、内连接（INNER JOIN）：只保留 “双方匹配” 的数据

内连接是最严格的连接方式，**仅返回两个表中 “关联字段完全匹配” 的行**，不匹配的行（如 “有用户但无订单”“有订单但无对应用户”）会被过滤掉。

#### 1. 核心逻辑

- 匹配条件：两个表的关联字段（如 `users.user_id = orders.user_id`）必须相等。
- 结果范围：仅包含 “既在表 A 有记录，又在表 B 有对应记录” 的数据。

#### 2. 示例 SQL

```sql
SELECT u.user_id, u.user_name, o.order_id, o.order_amount
FROM users u
INNER JOIN orders o 
  ON u.user_id = o.user_id; -- 关联条件
```

#### 3. 结果表（内连接结果）

| user_id | user_name | order_id | order_amount |
| ------- | --------- | -------- | ------------ |
| 1       | 张三      | 101      | 100          |
| 1       | 张三      | 102      | 200          |
| 2       | 李四      | 103      | 150          |

- 说明：王五（user_id=3）因无订单，未出现在结果中；若订单表有 “无对应用户” 的订单（如 user_id=4），也会被过滤。

### 三、外连接（OUTER JOIN）：保留 “某一侧所有数据”，匹配不到补 NULL

外连接的核心是 **“不丢弃某一侧的所有数据”**，即使另一侧没有匹配的记录，也会保留该侧数据，并将另一侧的字段值设为 `NULL`（空值）。
外连接分为**左连接、右连接、全外连接 **，其中左 / 右连接是实际开发中最常用的。

#### 1. 左连接（LEFT JOIN / LEFT OUTER JOIN）：保留 “左表所有数据”

左连接以**左侧表（SQL 中 `LEFT JOIN` 左边的表）为基准**，保留左表的所有行，右侧表仅保留与左表匹配的行；若右侧表无匹配，右侧字段值补 `NULL`。

##### （1）核心逻辑

- 基准表：左表（如示例中的 `users`），所有行必保留。
- 匹配规则：右表（如 `orders`）有匹配则显示，无匹配则右表字段为 `NULL`。

##### （2）示例 SQL

```sql
SELECT u.user_id, u.user_name, o.order_id, o.order_amount
FROM users u -- 左表
LEFT JOIN orders o -- 右表
  ON u.user_id = o.user_id;
```

##### （3）结果表（左连接结果）

| user_id | user_name | order_id | order_amount |
| ------- | --------- | -------- | ------------ |
| 1       | 张三      | 101      | 100          |
| 1       | 张三      | 102      | 200          |
| 2       | 李四      | 103      | 150          |
| 3       | 王五      | NULL     | NULL         |

- 关键变化：王五（左表数据）即使无订单，仍被保留，右侧 `order_id` 和 `order_amount` 补 `NULL`。

#### 2. 右连接（RIGHT JOIN / RIGHT OUTER JOIN）：保留 “右表所有数据”

右连接与左连接逻辑对称，以**右侧表（SQL 中 `RIGHT JOIN` 右边的表）为基准**，保留右表的所有行，左表仅保留匹配的行；若左表无匹配，左表字段值补 `NULL`。

##### （1）核心逻辑

- 基准表：右表（如示例中的 `orders`），所有行必保留。
- 匹配规则：左表（如 `users`）有匹配则显示，无匹配则左表字段为 `NULL`。

##### （2）示例 SQL（新增一条 “无对应用户” 的订单）

先给 `orders` 表加一条数据：`order_id=104, user_id=4, order_amount=300`（user_id=4 在 users 表中不存在），再执行右连接：

```sql
SELECT u.user_id, u.user_name, o.order_id, o.order_amount
FROM users u -- 左表
RIGHT JOIN orders o -- 右表
  ON u.user_id = o.user_id;
```

##### （3）结果表（右连接结果）

| user_id | user_name | order_id | order_amount |
| ------- | --------- | -------- | ------------ |
| 1       | 张三      | 101      | 100          |
| 1       | 张三      | 102      | 200          |
| 2       | 李四      | 103      | 150          |
| NULL    | NULL      | 104      | 300          |

- 关键变化：订单 104（右表数据）即使无对应用户，仍被保留，左侧 `user_id` 和 `user_name` 补 `NULL`；王五（左表无匹配）则被丢弃。

#### 3. 全外连接（FULL JOIN / FULL OUTER JOIN）：保留 “两侧所有数据”

全外连接是左连接 + 右连接的组合，**保留两个表的所有行**：

- 若双方有匹配，正常显示；
- 若左表无匹配，右表字段补 `NULL`；
- 若右表无匹配，左表字段补 `NULL`。

##### （1）示例结果（基于上述扩展表）

| user_id | user_name | order_id | order_amount |
| ------- | --------- | -------- | ------------ |
| 1       | 张三      | 101      | 100          |
| 1       | 张三      | 102      | 200          |
| 2       | 李四      | 103      | 150          |
| 3       | 王五      | NULL     | NULL         |
| NULL    | NULL      | 104      | 300          |

##### （2）注意

并非所有数据库都支持全外连接，例如 **MySQL 不原生支持 `FULL JOIN`**，需通过 `LEFT JOIN + UNION + RIGHT JOIN` 模拟实现。

### 四、四种连接的核心区别对比

为了更清晰区分，用表格总结关键差异（基于示例表）：

| 连接类型         | 基准表         | 保留数据范围            | 不匹配时处理    | 示例结果包含的关键行                                       |
| ---------------- | -------------- | ----------------------- | --------------- | ---------------------------------------------------------- |
| 内连接（INNER）  | 无（双方匹配） | 仅双方匹配的行          | 过滤不匹配行    | 张三（2 行）、李四（1 行）                                 |
| 左连接（LEFT）   | 左表（users）  | 左表所有行 + 右表匹配行 | 右表字段补 NULL | 张三（2 行）、李四（1 行）、王五（1 行）                   |
| 右连接（RIGHT）  | 右表（orders） | 右表所有行 + 左表匹配行 | 左表字段补 NULL | 张三（2 行）、李四（1 行）、订单 104（1 行）               |
| 全外连接（FULL） | 两侧表         | 两侧所有行 + 双方匹配行 | 无匹配侧补 NULL | 张三（2 行）、李四（1 行）、王五（1 行）、订单 104（1 行） |

### 五、实际开发中的选择建议

1. **查 “双方都存在” 的关联数据**：用内连接（如 “查有订单的用户及其订单”）。
2. **查 “左表所有数据，关联右表信息”**：用左连接（如 “查所有用户，包括无订单的用户，显示其订单（若无则空）”）。
3. **查 “右表所有数据，关联左表信息”**：用右连接（如 “查所有订单，包括无对应用户的异常订单，显示用户信息（若无则空）”）。
4. **查 “两侧所有数据，不遗漏任何一方”**：用全外连接（如 “统计所有用户和所有订单，包括无关联的记录”，需注意数据库兼容性）。





## SQLAlchemy中的子查询subquery

![image-20250913102917486](assets/image-20250913102917486.png) 

SQLAlchemy 实现子查询的核心步骤可概括为：



1. **写内层查询**：用 `select()` 构建需要嵌入的查询逻辑，给字段命名；
2. **转子查询表**：调用 `subquery()` 将内层查询转换为 `Subquery` 对象；
3. **写外层查询**：将子查询当作 “临时表”，通过 `join`/`select_from`/`where` 等操作引用；
4. **执行查询**：通过 `Session.execute()` 获取结果。



### 一、子查询的核心原理

SQLAlchemy 中，子查询本质是将一个 `select()` 构建的查询对象，通过 **`subquery()` 方法** 转换为 “可嵌入的子查询表”（`Subquery` 对象），该对象可像普通表一样被外层查询引用（如用于 `join`、`select_from` 等操作）。

关键规则：

- 子查询必须通过 `subquery()` 方法显式转换（SQLAlchemy 1.4+ 不再支持直接将 `Select` 作为 `FROM` 子句）；
- 子查询的字段可通过 `c` 属性引用（如 `subq.c.user_id`，`c` 即 `columns` 的缩写）。

### 二、通用实现步骤（以 `FROM` 子句子查询为例）

以 “先统计每个用户的订单数（子查询），再查询订单数大于 1 的用户” 为例，演示完整步骤：

#### 步骤 1：导入必要组件

需导入 `select`（构建查询）、`func`（聚合函数）等核心组件：

```python
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session
from models import User, Order  # 假设已定义User（用户表）、Order（订单表）模型
from db_util import engine  # 假设已创建数据库引擎
```

#### 步骤 2：构建 “子查询”（统计每个用户的订单数）

先定义内层查询，统计 `Order` 表中每个 `user_id` 对应的订单数量，再通过 `subquery()` 转换为子查询表：

```python
# 2.1 构建内层查询：统计每个user_id的订单数，命名为order_count
inner_stmt = select(
    Order.user_id,  # 子查询字段1：用户ID（关联外层User表）
    func.count(Order.id).label("order_count")  # 子查询字段2：订单数，用label()命名（方便外层引用）
).group_by(Order.user_id)  # 按user_id分组（每个用户一组）

# 2.2 转换为子查询表，命名为subq（可选，默认生成匿名子查询）
subq = inner_stmt.subquery(name="user_order_count")  # name参数给子查询起别名，便于SQL可读性
```

- `label("order_count")`：给聚合结果列起别名，避免外层引用时出现 “匿名列” 问题；
- `subq` 此时是 `Subquery` 对象，可被外层查询当作 “临时表” 使用。

#### 步骤 3：构建 “外层查询”（引用子查询，筛选订单数 > 1 的用户）

外层查询将 `User` 表与子查询表 `subq` 关联，筛选出订单数大于 1 的用户信息：

```python
# 3.1 外层查询：关联User表和子查询表，筛选order_count>1的用户
outer_stmt = select(
    User.id,  # 外层查询字段1：用户ID
    User.name,  # 外层查询字段2：用户名
    subq.c.order_count  # 引用子查询的字段：订单数（通过subq.c.字段名）
).join(
    subq,  # 关联的子查询表
    User.id == subq.c.user_id  # 关联条件：User.id = 子查询的user_id
).where(
    subq.c.order_count > 1  # 筛选条件：订单数大于1
)
```

- `subq.c.user_id`/`subq.c.order_count`：通过 `c` 属性引用子查询的字段，`c` 是 `subq.columns` 的简写；
- `join(subq, ...)`：将子查询表与主表（User）进行内连接，仅保留有订单统计的用户。

#### 步骤 4：执行查询并获取结果

通过 `Session` 执行外层查询，获取最终结果：

```python
with Session(engine) as session:
    result = session.execute(outer_stmt).all()
    print(result)
    # 示例输出：[(1, '张三', 2), (3, '王五', 3)]（用户1有2个订单，用户3有3个订单）
```

### 三、其他常见子查询场景示例

#### 场景 1：`WHERE` 子句中的子查询（ EXISTS / IN ）

需求：查询 “有订单的用户”（即 `user.id` 存在于 `Order.user_id` 中的用户），用 `EXISTS` 子查询实现：

```python
# 子查询：获取所有有订单的user_id
inner_stmt = select(Order.user_id).distinct()  # distinct()去重，避免重复user_id
subq = inner_stmt.subquery()

# 外层查询：筛选存在于子查询中的用户
outer_stmt = select(User).where(
    User.id.in_(subq.c.user_id)  # IN子查询：User.id在子查询的user_id中
    # 或用EXISTS：exists(select(1).where(Order.user_id == User.id))
)

# 执行
with Session(engine) as session:
    users_with_order = session.execute(outer_stmt).scalars().all()
    print(users_with_order)
```

#### 场景 2：关联多个子查询

需求：同时关联 “用户订单数” 和 “用户订单总金额” 两个子查询，查询用户的综合信息：

```python
# 子查询1：统计每个用户的订单数
subq1 = select(
    Order.user_id,
    func.count(Order.id).label("order_count")
).group_by(Order.user_id).subquery(name="subq_count")

# 子查询2：统计每个用户的订单总金额
subq2 = select(
    Order.user_id,
    func.sum(Order.amount).label("total_amount")
).group_by(Order.user_id).subquery(name="subq_sum")

# 外层查询：关联User表和两个子查询
outer_stmt = select(
    User.name,
    subq1.c.order_count,
    subq2.c.total_amount
).join(subq1, User.id == subq1.c.user_id)  # 关联订单数子查询
.join(subq2, User.id == subq2.c.user_id)  # 关联总金额子查询

# 执行
with Session(engine) as session:
    result = session.execute(outer_stmt).all()
    print(result)
    # 示例输出：[('张三', 2, 300), ('王五', 3, 500)]
```

### 四、关键注意事项

1. **子查询字段必须命名**：
    子查询中的字段（尤其是聚合结果）需用 `label("字段名")` 命名，否则外层无法通过 `subq.c.字段名` 引用（会出现 `NoSuchColumnError`）。
2. **子查询需显式转换**：
    SQLAlchemy 1.4+ 要求子查询必须通过 `subquery()` 转换，直接将 `Select` 对象嵌入外层查询会报错（如 `Expected FROM clause, got Select`）。
3. **关联条件需明确**：
    外层查询与子查询关联时，需指定清晰的关联条件（如 `User.id == subq.c.user_id`），避免笛卡尔积（数据重复）。
4. **性能优化**：
    子查询若涉及大量数据，建议：
    - 给子查询的关联字段（如 `user_id`）加索引；
    - 复杂场景可改用 `CTE`（公共表表达式，`with_cte()` 方法），可读性和性能更优。





## SQLAlchemy中的aliased函数

![image-20250913111817788](assets/image-20250913111817788.png) 

​	在 SQLAlchemy 中，`aliased()` 函数用于为表、子查询或其他可别名化的构造创建别名（alias），这在处理自连接（self-join）或需要多次引用同一表时特别有用。

### 主要用途：

1. 处理自连接（同一表与自身连接）
2. 简化复杂查询中对同一表的多次引用
3. 为子查询或 CTE (公用表表达式) 创建可读性更好的名称

### 基本用法示例：

假设我们有一个 `User` 表模型，需要查询用户及其推荐人（也是用户）：

```python
from sqlalchemy.orm import aliased
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    referrer_id = Column(Integer, ForeignKey('users.id'))  # 自引用外键

# 创建别名
Referrer = aliased(User)

# 创建会话
engine = create_engine('sqlite:///mydb.db')
Session = sessionmaker(bind=engine)
session = Session()

# 查询用户及其推荐人
query = session.query(
    User.name.label('user_name'),
    Referrer.name.label('referrer_name')
).join(
    Referrer, User.referrer_id == Referrer.id, isouter=True
)

# 执行查询
for result in query.all():
    print(f"用户: {result.user_name}, 推荐人: {result.referrer_name}")
```

### 对子查询使用别名：

```python
from sqlalchemy import select

# 创建子查询并别名化
subquery = select(User.id, User.name).where(User.referrer_id.is_(None)).subquery()
NewUsers = aliased(subquery)

# 使用别名化的子查询
query = select(NewUsers.c.id, NewUsers.c.name)
```

### 关键点：

- `aliased()` 可以接受表模型、表对象或子查询作为参数
- 创建的别名可以像原表一样使用，但需要通过别名引用其列
- 对于 ORM 模型，别名对象会保留原模型的所有属性和关系
- 对于子查询，需要通过 `.c` 属性访问列（如 `NewUsers.c.id`）

使用 `aliased()` 可以使复杂查询的代码更清晰、更易读，尤其在处理多表连接或自连接时非常有价值。



## Flask-SQLAlchemy的使用

![image-20250913154333024](assets/image-20250913154333024.png) 

Flask-SQLAlchemy 是 Flask 框架的一个扩展，它简化了在 Flask 应用中使用 SQLAlchemy 的过程。SQLAlchemy 是一个强大的 Python ORM（对象关系映射）工具，允许开发者使用 Python 类和对象来操作数据库，而不必直接编写 SQL 语句。

### 核心特点：

- 简化了 SQLAlchemy 与 Flask 的集成
- 提供了更简洁的 API 用于数据库操作
- 自动处理数据库连接的创建和关闭
- 支持多种数据库后端（SQLite、MySQL、PostgreSQL 等）
- 与 Flask 的上下文系统无缝集成

### Flask-SQLAlchemy的使用

#### 数据库连接

数据库初始化不再是通过`create_engine`

1. 定义数据库连接字符串`DB_URI`

2. 配置数据库URI

    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    ```

3. 使用`flask_sqlalchemy.SQLAlchemy`这个类定义一个对象,并将`app`传入

    ```python
    db = SQLAlchemy(app)
    ```

#### 创建ORM模型类

1. 使用`db.Model`作为基类,定义模型
2. 在模型类中,可以直接使用`db.Column`、`db.String`、`db.Integer`、`db.relationship`等
3. 定义模型时,可以不写`__tablename__`,`flask_sqlalchemy`会默认使用当前模型的名字转换成小写来作为表名,如果这个模型的名字用到多个单词并且使用了驼峰命名法,那么会在多个单词之间使用下划线进行连接(不推荐使用)

#### 将ORM模型映射到数据库表

​	定义好模型后,可以使用以下代码将模型映射到数据库的表中

1. 删除数据库表:`db.drop_all()`
2. 创建数据库表:`db.create_all()`



**session的使用**

不需要使用`sessionmaker`来创建,可以直接使用`db.session`



**查询数据**

- 单表查询:使用`模型名.query`进行查询
- 多表查询:使用`db.session.query(模型名).all()`



```python
# 导入Flask框架和Flask-SQLAlchemy扩展
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 注意：from mypy.types import names 这行没有实际使用，可以删除
from sqlalchemy.orm import backref

# 初始化Flask应用
app = Flask(__name__)

# 数据库连接配置信息
HOST = 'localhost'       # 数据库主机地址
PORT = 3306              # 数据库端口号，MySQL默认3306
DATA_BASE = 'test'       # 数据库名称
USER = 'root'            # 数据库用户名
PWD = '123456'           # 数据库密码

# 构建数据库连接URI
DB_URI = f'mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DATA_BASE}'

# Flask-SQLAlchemy配置
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭修改跟踪，提高性能
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI        # 设置数据库连接URI

# 初始化SQLAlchemy对象，关联Flask应用
db = SQLAlchemy(app)

# 定义User模型类，对应数据库中的表
class User(db.Model):
    __tablename__ = 't_user'  # 指定数据库表名，不写则默认使用类名小写
    # 定义id字段：整数类型，主键，自增
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 定义name字段：字符串类型，长度32
    name = db.Column(db.String(32))

    # 定义对象的字符串表示，方便调试时查看
    def __repr__(self):
        return f'<User: id={self.id} name={self.name}>'

# 定义News模型类，对应数据库中的新闻表
class News(db.Model):
    __tablename__ = 't_news'  # 指定数据库表名
    # 定义id字段：整数类型，主键，自增
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 定义content字段：字符串类型，长度100，存储新闻内容
    content = db.Column(db.String(100))
    # 定义外键字段uid，关联到t_user表的id字段
    uid = db.Column(db.Integer, db.ForeignKey('t_user.id'))

    # 定义与User模型的关系：
    # 1. 在News对象中通过user属性可以访问对应的User对象
    # 2. backref定义反向引用，在User对象中通过news属性可以访问关联的所有News对象
    # 3. lazy=True表示使用惰性加载，访问时才会实际查询数据库
    user = db.relationship('User', backref=db.backref('news', lazy=True))

    # 定义对象的字符串表示，方便调试时查看
    def __repr__(self):
        return f'<News: id={self.id} content={self.content}>'


# 增加数据函数
def add_data():
    # 使用with语句确保在应用上下文中执行数据库操作
    with app.app_context():
        # 创建User对象
        user = User(name='bob')
        # 创建News对象
        news = News(content='python')
        # 通过关系属性将新闻添加到用户的新闻列表中
        user.news.append(news)
        # 将用户对象添加到会话中（此时新闻对象会被自动关联添加）
        db.session.add(user)
        # 提交会话，将数据写入数据库
        db.session.commit()

# 查询单表数据函数
def query_data():
    with app.app_context():
        # 查询User表中的所有记录，返回User对象列表
        users = User.query.all()
        # 打印查询结果
        print(users)

# 查询多表数据函数（关联查询）
def query_data_many():
    with app.app_context():
        # 多表连接查询：通过join方法关联User和News表
        # 条件是News表的uid等于User表的id
        # all()方法返回所有匹配的结果，每个结果是(User对象, News对象)的元组
        rs = db.session.query(User, News).join(News, News.uid == User.id).all()
        # 打印查询结果
        print(rs)

# 更新数据函数
def updata_data():  # 注意：函数名应该是update_data，这里修正了拼写错误
    with app.app_context():
        # 查询User表中的第一条记录
        user = User.query.first()
        # 修改用户的name属性
        user.name = 'jack'
        # 打印修改后的用户对象
        print(user)
        # 提交会话，将修改保存到数据库
        db.session.commit()


if __name__ == '__main__':
    # 以下代码为不同操作的示例，通过注释/取消注释来执行不同功能
    # 1. 创建数据库表（首次运行时需要执行）
    # with app.app_context():
    #     db.drop_all()  # 先删除所有表（谨慎使用，会清除数据）
    #     db.create_all()  # 创建所有模型对应的表

    # 2. 执行添加数据操作
    # add_data()
    
    # 3. 执行单表查询操作
    # query_data()
    
    # 4. 执行多表关联查询操作
    # query_data_many()
    
    # 5. 执行更新数据操作
    updata_data()
```





## 数据库迁移工具alembic的使用

![image-20250913163908625](assets/image-20250913163908625.png)

### alembic的使用

<img src="assets/image-20250913164453773.png" alt="image-20250913164453773" style="zoom:67%;" /> 

Alembic 是 SQLAlchemy 官方推出的 **数据库版本控制工具**，核心作用是管理数据库表结构的变更（如新增表、修改字段、删除索引等），避免手动修改数据库导致的版本混乱，尤其适合多人协作或多环境（开发 / 测试 / 生产）同步场景。



以下是 Alembic 的 **完整使用流程**，从环境准备到版本迁移，结合常见操作场景说明：

### 一、前置准备：安装依赖与初始化项目

在使用 Alembic 前，需确保项目已满足基础环境，并完成 Alembic 初始化。

#### 1. 安装依赖

需安装 `alembic` 和 `sqlalchemy`（若用 Flask 则需 `flask-sqlalchemy`），命令如下：

```bash
# 基础安装（SQLAlchemy 项目）
pip install alembic sqlalchemy

# Flask 项目额外安装
pip install flask-sqlalchemy
```

#### 2. 初始化 Alembic（核心步骤）

进入项目根目录（需提前创建好项目，如 `23_alembic_demo`），执行 `alembic init 目录名`（通常目录名用 `alembic`，默认即可）：

```bash
# 初始化 Alembic，生成 alembic 目录和 alembic.ini 配置文件
alembic init alembic
```



执行后，项目根目录会生成两个关键文件 / 目录：



- `alembic/`：Alembic 核心目录，包含版本文件、环境配置等；
- `alembic.ini`：Alembic 全局配置文件，主要配置数据库连接地址。

### 二、关键配置：关联数据库与模型

初始化后，需修改两个配置文件，让 Alembic 知道 **连接哪个数据库** 以及 **对应哪个项目的模型类**。

#### 1. 配置数据库连接（alembic.ini）

打开 `alembic.ini`，找到 `sqlalchemy.url` 字段，替换为项目的数据库 URI（格式与 SQLAlchemy 一致）：



```ini
# 原配置（注释状态）
# sqlalchemy.url = driver://user:pass@localhost:port/dbname

# 实际配置（以 MySQL 为例，需安装 pymysql：pip install pymysql）
sqlalchemy.url = mysql+pymysql://root:123456@localhost:3306/test_db

# 若为 SQLite（无需密码，文件路径在项目内）
# sqlalchemy.url = sqlite:///./test.db

# 若为 PostgreSQL（需安装 psycopg2：pip install psycopg2-binary）
# sqlalchemy.url = postgresql://user:pass@localhost:5432/test_db
```



> 注意：确保数据库（如 `test_db`）已提前创建（Alembic 不自动创建数据库，仅管理表结构）。

#### 2. 关联项目模型（alembic/env.py）

Alembic 需读取项目中的 **SQLAlchemy 模型类**（如 `User`、`News`），才能自动对比模型与数据库的差异。需修改 `alembic/env.py` 中的 `target_metadata` 变量：

##### 场景 1：纯 SQLAlchemy 项目（非 Flask）

假设项目模型定义在 `models.py` 中（如：`from models import Base`，`Base` 是 `declarative_base()` 实例）：



```python
# 打开 alembic/env.py，找到 target_metadata 相关代码
# 1. 导入项目的 Base 类（模型的基类）
from models import Base  # 替换为你项目的模型基类路径

# 2. 将 target_metadata 赋值为 Base.metadata
target_metadata = Base.metadata  # 原代码是 target_metadata = None，需修改
```

##### 场景 2：Flask-SQLAlchemy 项目

Flask 项目的模型通常通过 `db = SQLAlchemy(app)` 或 `db = SQLAlchemy()` 初始化，需先加载 Flask 上下文，再关联模型：

```python
# 打开 alembic/env.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from alembic import context

# 1. 初始化 Flask 应用（模拟项目启动）
app = Flask(__name__)
# 配置数据库连接（需与 alembic.ini 一致，或直接读取 alembic.ini 配置）
app.config['SQLALCHEMY_DATABASE_URI'] = context.config.get_main_option("sqlalchemy.url")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 2. 初始化 db 并导入模型
db = SQLAlchemy(app)
from models import User, News  # 导入项目所有模型类（或导入模型基类）

# 3. 关联模型元数据
target_metadata = db.metadata  # 关键：将 db 的元数据赋值给 target_metadata
```



> 核心原则：`target_metadata` 必须指向项目中 **所有模型的基类元数据**（纯 SQLAlchemy 是 `Base.metadata`，Flask 是 `db.metadata`），否则 Alembic 无法自动识别模型变更。

### 三、核心流程：生成版本文件与执行迁移

Alembic 的核心操作围绕 **“版本文件”** 展开：通过模型生成版本文件，再执行版本文件同步到数据库。

#### 1. 生成版本文件（自动对比模型与数据库）

当项目模型发生变更（如新增表、修改字段类型、删除索引）后，执行以下命令，Alembic 会 **自动对比当前模型与数据库的差异**，生成一个 “版本文件”（记录变更逻辑）：

```bash
alembic revision --autogenerate -m "版本描述"
```

- `--autogenerate`：自动检测模型与数据库的差异（无需手动写 SQL）；
- `-m "版本描述"`：给当前版本添加备注，如 “add user table”“modify news content field”，方便后续追溯。

**执行后效果**：
在 `alembic/versions/` 目录下会生成一个以 `时间戳_版本描述.py` 命名的文件（如 `20240913_123456_add_user_table.py`），文件内包含两个核心函数：

- `upgrade()`：执行 “升级” 操作（如创建表、新增字段）；
- `downgrade()`：执行 “回滚” 操作（如删除表、恢复旧字段），确保版本可回退。

> 注意：`--autogenerate` 并非万能，以下场景需手动修改版本文件：
>
> - 新增索引 / 外键约束；
> - 字段类型从 `INT` 改为 `BIGINT`（部分数据库需手动写 SQL）；
> - 删除表或字段（Alembic 默认不自动生成删除逻辑，需手动确认）。

#### 2. 执行迁移（同步版本文件到数据库）

生成版本文件后，需执行以下命令，将版本文件中的 `upgrade()` 逻辑应用到数据库，完成表结构同步：

```bash
# 执行最新版本的迁移（推荐，自动同步到最新版本）
alembic upgrade head

# 可选：指定迁移到某个版本（版本号是 versions 目录下文件的前缀，如 20240913_123456）
alembic upgrade 20240913_123456

# 可选：迁移到上一个版本（相对迁移，+1 表示下一个版本）
alembic upgrade +1
```

执行成功后，数据库会自动创建 / 修改表结构，同时生成一个 `alembic_version` 表（记录当前数据库的 Alembic 版本，避免重复迁移）。

### 四、常用辅助操作

在日常开发中，常需查看版本状态、回滚版本或重置环境，以下是高频操作：

#### 1. 查看当前数据库版本

查看当前数据库对应的 Alembic 版本，确认是否与本地版本一致：

```bash
alembic current
```

#### 2. 查看版本历史

查看所有已生成的版本文件，包括版本号、描述、创建时间：

```bash
alembic history

# 简化输出（仅显示版本号和描述）
alembic history --compact
```

#### 3. 回滚版本

若迁移后发现问题，可回滚到之前的版本（执行 `downgrade()` 逻辑）：

```bash
# 回滚到上一个版本
alembic downgrade -1

# 回滚到指定版本（版本号前缀）
alembic downgrade 20240912_098765

# 回滚到最初版本（删除所有表结构，谨慎使用！）
alembic downgrade base
```

#### 4. 手动创建版本文件（无自动对比）

若需手动编写 SQL 逻辑（如复杂的表结构调整），可跳过 `--autogenerate`，直接创建空的版本文件：

```bash
alembic revision -m "手动调整 user 表字段"
```



然后打开生成的版本文件，手动在 `upgrade()` 和 `downgrade()` 中编写 SQLAlchemy 代码（如 `op.add_column()`、`op.drop_table()`）。

#### 5. 重置 Alembic 环境（谨慎使用）

若版本文件混乱，需重新开始版本控制，可执行以下步骤（会删除现有版本记录）：



1. 删除 `alembic/versions/` 目录下所有版本文件；
2. 删除数据库中的 `alembic_version` 表；
3. 重新执行 `alembic revision --autogenerate -m "init db"` 生成初始版本；
4. 执行 `alembic upgrade head` 同步到数据库。

### 五、常见问题与注意事项

1. **“declarative_base () takes 0 positional arguments” 错误**
    原因：`declarative_base()` 是无参函数，若写成 `declarative_base(engine)` 会报错。
    解决：模型基类定义应为 `Base = declarative_base()`，引擎通过 `Base.metadata.create_all(engine)` 关联，而非传入 `declarative_base`。
2. **`--autogenerate` 无法识别模型变更**
    原因：`alembic/env.py` 中 `target_metadata` 未正确关联项目模型，或模型路径导入错误。
    解决：确认 `target_metadata` 指向模型基类的 `metadata`（如 `Base.metadata` 或 `db.metadata`），且导入路径正确（避免相对路径问题，可使用绝对路径）。
3. **生产环境迁移注意事项**
    - 迁移前必须备份数据库（防止 `upgrade` 失败导致数据丢失）；
    - 先在测试环境验证迁移脚本，再在生产环境执行；
    - 避免在高峰期执行迁移（尤其是添加索引、修改大表字段，可能锁表）。

### 六、流程总结（核心步骤）

1. 初始化：`alembic init alembic`；
2. 配置：修改 `alembic.ini`（数据库连接）和 `alembic/env.py`（关联模型）；
3. 生成版本：`alembic revision --autogenerate -m "描述"`；
4. 执行迁移：`alembic upgrade head`；
5. 回滚 / 查看：`alembic downgrade -1` 或 `alembic history`。



## alembic常见错误以及解决办法

![image-20250913180752159](assets/image-20250913180752159.png) 

**以下是 Alembic 开发中常见的错误、原因及解决办法，以表格形式整理：**



| 错误信息示例                                                 | 可能原因                                                     | 解决办法                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `TypeError: declarative_base() takes 0 positional arguments but 1 was given` | 模型基类定义时错误地向 `declarative_base()` 传递了参数（如 `declarative_base(engine)`） | `declarative_base()` 无需参数，正确写法：`Base = declarative_base()`，引擎通过 `Base.metadata.create_all(engine)` 关联 |
| `Target database is not up to date.`                         | 数据库当前版本与本地版本文件不一致，存在未执行的迁移         | 执行 `alembic upgrade head` 同步到最新版本                   |
| `No changes in schema detected.`                             | `--autogenerate` 未检测到模型与数据库的差异                  | 1. 检查 `alembic/env.py` 中 `target_metadata` 是否正确关联模型元数据 2. 确认模型类已被导入（Flask 项目需加载上下文） 3. 手动修改过数据库表结构，导致与模型同步失败 |
| `Can't locate revision identified by 'xxx'`                  | 尝试迁移到一个不存在的版本号（如版本文件被删除）             | 1. 检查版本号是否正确（查看 `alembic/versions/` 目录） 2. 若版本文件丢失，需重新生成或从备份恢复 |
| `(pymysql.err.OperationalError) (1045, "Access denied for user 'xxx'@'localhost'")` | 数据库连接信息错误（用户名、密码、主机等）                   | 1. 检查 `alembic.ini` 中 `sqlalchemy.url` 是否正确 2. 确认数据库用户权限及密码是否有效 |
| `Table 'xxx' already exists`                                 | 手动创建过表，与 Alembic 自动生成的表冲突                    | 1. 删除手动创建的表，由 Alembic 重新生成 2. 执行 `alembic stamp head` 将现有表标记为最新版本（不执行迁移逻辑） |
| `Foreign key constraint failed`                              | 回滚或迁移时外键约束冲突（如删除被引用的表）                 | 1. 先删除依赖外键的表数据或表结构 2. 在版本文件的 `downgrade()` 中调整执行顺序，确保先删除子表再删除父表 |
| `alembic: error: argument command: invalid choice: 'xxx'`    | 输入了错误的 Alembic 命令（如 `alembic pwd`）                | 查看帮助文档：`alembic --help`，使用正确命令（如 `upgrade`、`revision`） |
| `ImportError: cannot import name 'Base' from 'models'`       | `alembic/env.py` 中模型导入路径错误                          | 1. 检查导入语句是否正确（使用绝对路径或项目根目录添加到 `sys.path`） 2. 确保模型文件存在且 `Base` 类已定义 |
| `DatabaseError: (cx_Oracle.DatabaseError) ORA-00955: name is already used by an existing object` | Oracle 数据库中存在同名对象（如表、索引）                    | 1. 删除同名对象或修改模型的 `__tablename__` 避免冲突 2. 在版本文件中手动处理冲突逻辑 |



## Flask-SQLAlchemy和alembic结合使用

![image-20250913181414634](assets/image-20250913181414634.png) 

将 Flask-SQLAlchemy 与 Alembic 结合使用，可以实现 Flask 项目中数据库表结构的版本化管理。以下是详细的步骤指南：

### **一、环境准备**

1. **安装依赖**
    确保已安装必要的包：

    ```bash
    pip install flask flask-sqlalchemy alembic pymysql  # pymysql 用于 MySQL 连接，按需替换
    ```

2. **项目结构**
    假设项目结构如下（后续步骤将基于此结构操作）：

    ```plaintext
    my_flask_project/
    ├── app.py               # Flask 应用主文件（含模型定义）
    └── config.py            # 配置文件（数据库连接等）
    ```

### **二、初始化 Flask 项目与模型**

1. **创建配置文件（config.py）**
    配置数据库连接信息：

    ```python
    # config.py
    import os
    
    # 数据库连接 URI（MySQL 示例，其他数据库需调整格式）
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/my_flask_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 关闭修改跟踪，提升性能
    ```

2. **创建 Flask 应用与模型（app.py）**
    定义 Flask 应用、初始化 `db` 对象，并创建数据模型：

    ```python
    # app.py
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    import config
    
    # 初始化 Flask 应用
    app = Flask(__name__)
    app.config.from_object(config)  # 加载配置
    
    # 初始化 SQLAlchemy
    db = SQLAlchemy(app)
    
    # 定义模型（示例：用户表和文章表）
    class User(db.Model):
        __tablename__ = "users"
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        username = db.Column(db.String(50), unique=True, nullable=False)
        email = db.Column(db.String(100), unique=True, nullable=False)
    
    class Article(db.Model):
        __tablename__ = "articles"
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        title = db.Column(db.String(100), nullable=False)
        content = db.Column(db.Text)
        author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
        
        # 关联 User 模型
        author = db.relationship("User", backref=db.backref("articles"))
    
    # 确保在应用上下文内使用（非必要，仅用于测试）
    if __name__ == "__main__":
        with app.app_context():
            db.create_all()  # 临时创建表（后续将由 Alembic 接管）
        app.run(debug=True)
    ```

### **三、初始化 Alembic**

1. 创建 Alembic 配置

    在项目根目录执行以下命令，生成 Alembic 所需的目录和配置文件：

    ```bash
    alembic init alembic
    ```

    执行后，项目结构会新增：

    - `alembic/`：Alembic 核心目录（版本文件、环境配置等）
    - `alembic.ini`：Alembic 全局配置文件

### **四、配置 Alembic 关联 Flask-SQLAlchemy**

#### 1. **配置数据库连接（alembic.ini）**

打开 `alembic.ini`，修改 `sqlalchemy.url` 为项目的数据库连接 URI（需与 `config.py` 一致）：

```ini
# alembic.ini
sqlalchemy.url = mysql+pymysql://root:123456@localhost:3306/my_flask_db
```

#### 2. **关联 Flask 模型（alembic/env.py）**

关键步骤：让 Alembic 识别 Flask-SQLAlchemy 的模型，以便自动生成迁移脚本。
修改 `alembic/env.py` 中的 `target_metadata` 配置：

```python
# alembic/env.py
import os
import sys
from logging.config import fileConfig

from alembic import context
from flask import current_app

# 将项目根目录添加到 Python 路径（确保能导入 app 和 config）
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app import db  # 导入 Flask-SQLAlchemy 的 db 对象
import config  # 导入项目配置

# 初始化 Flask 应用上下文（关键：Alembic 需要应用上下文才能访问 db）
config = context.config
fileConfig(config.config_file_name)

# 关联 Flask-SQLAlchemy 的元数据（模型信息）
target_metadata = db.metadata  # 核心：指向 db 的元数据


# 以下为默认生成的迁移逻辑（无需修改）
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = current_app.extensions["sqlalchemy"].engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

### **五、生成与执行迁移脚本**

#### 1. **生成初始迁移脚本**

首次使用时，生成初始版本的迁移脚本（基于当前模型）：

```bash
alembic revision --autogenerate -m "初始化数据库：创建 users 和 articles 表"
```

- `--autogenerate`：自动对比模型与数据库的差异（需确保模型已导入）
- `-m`：添加迁移备注（描述本次变更）

执行成功后，`alembic/versions/` 目录会生成一个以时间戳开头的迁移文件（如 `20240915_123456_初始化数据库...py`）。

#### 2. **执行迁移（同步到数据库）**

将迁移脚本应用到数据库，创建表结构：

```bash
alembic upgrade head
```



- `head` 表示迁移到最新版本。执行后，数据库会生成模型对应的表，以及一个 `alembic_version` 表（记录当前数据库版本）。

### **六、后续模型变更流程**

当模型发生修改（如新增字段、修改类型等），重复以下步骤：



1. **修改模型**（如在 `User` 表中新增 `age` 字段）：

    

    ```python
    # app.py 中修改 User 模型
    class User(db.Model):
        # ... 原有字段 ...
        age = db.Column(db.Integer, default=0)  # 新增字段
    ```

2. **生成新的迁移脚本**：

    ```bash
    alembic revision --autogenerate -m "User 表新增 age 字段"
    ```

3. **执行迁移**：

    ```bash
    alembic upgrade head
    ```

### **七、回滚操作（如需撤销迁移）**

若迁移后发现问题，可回滚到上一个版本：

```bash
# 回滚到上一个版本
alembic downgrade -1

# 回滚到指定版本（版本号为迁移文件前缀，如 20240915_123456）
alembic downgrade 20240915_123456
```





## Flask_Migrate

![image-20250913184153764](assets/image-20250913184153764.png) 

### 介绍

​	`flask-migrate`是`flask`的一个扩展模块,用于扩展数据库表结构,`flask-migrate`是基于`Alembic`进行的一个封装,并集成到`Flask`中,所有的迁移操作都是`Alembic`做的,它能追踪模型的变化,并将变化映射到数据库中功能

### **Flask-Migrate 完整使用流程**

#### 1. **环境准备**

- 安装依赖：

    ```bash
    pip install flask flask-sqlalchemy flask-migrate pymysql  # pymysql 按需替换为对应数据库驱动
    ```

#### 2. **初始化配置（代码中）**

在 Flask 项目中配置数据库并初始化 Migrate：

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # 导入 Migrate

app = Flask(__name__)

# 配置数据库连接（以 MySQL 为例）
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化 SQLAlchemy
db = SQLAlchemy(app)

# 定义数据模型（如 User 表）
class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))
    # 后续可新增字段（如 age、city）

# 初始化 Migrate（关联 app 和 db）
migrate = Migrate(app, db)  # 注意：变量名不要与导入的 Migrate 重名
```

#### 3. **初始化迁移环境（首次使用）**

在项目根目录执行以下命令，生成迁移所需的 `migrations` 目录（类似 Alembic 的配置）：

```bash
flask db init
```

- 执行后会生成 `migrations` 文件夹，包含迁移版本文件和配置，**只需执行一次**。

#### 4. **生成迁移脚本（模型变更时）**

当模型发生变更（新增表、修改字段等），执行以下命令生成迁移脚本：

```bash
flask db migrate -m "备注信息"  # 备注说明本次变更内容，如 "新增 User 表" 或 "添加 city 字段"
```

- 示例：`flask db migrate -m 'no1'`（首次生成 User 表的迁移脚本）
- 迁移脚本会保存在 `migrations/versions/` 目录，文件名以时间戳和备注命名。

#### 5. **执行迁移（同步到数据库）**

生成迁移脚本后，执行以下命令将变更应用到数据库：

```bash
flask db upgrade
```

- 示例：`flask db upgrade`（将 `no1` 版本的脚本应用到数据库，创建 `t_user` 表）
- 执行后，数据库会同步模型变更，同时生成 `alembic_version` 表记录当前版本。

#### 6. **后续模型变更（重复步骤 4-5）**

当模型再次修改（如新增字段 `city`）：

1. 修改模型代码（添加 `city = db.Column(db.String(32))`）；
2. 生成新迁移脚本：`flask db migrate -m 'no2'`（备注说明 “新增 city 字段”）；
3. 执行迁移：`flask db upgrade`（将变更同步到数据库）。

#### 7. **回滚操作（如需撤销变更）**

若迁移后发现问题，可回滚到指定版本：

```bash
# 查看历史版本（获取版本号）
flask db history

# 回滚到上一个版本
flask db downgrade -1

# 回滚到指定版本（版本号为迁移脚本前缀，如 83cffebb3f7d）
flask db downgrade 83cffebb3f7d
```



## Flask项目结构

![image-20250914011206444](assets/image-20250914011206444.png) 

​	在 Flask 项目开发中，合理的结构管理是保证代码可维护性、可扩展性的核心。随着项目从简单脚本向复杂应用演进，混乱的文件结构会导致开发效率急剧下降。以下将从 **基础结构（小型项目）** 到 **进阶结构（中大型项目）** 逐步拆解，并说明核心模块的作用、最佳实践及注意事项。

## 一、核心原则：为何需要结构管理？

在设计 Flask 项目结构时，需遵循以下 3 个原则，避免 “所有代码堆在 `app.py`” 的反模式：

1. **关注点分离**：将路由、模型、业务逻辑、配置等拆分为独立模块，避免单一文件职责过重。
2. **可扩展性**：新增功能（如用户模块、支付模块）时，只需在对应目录下新增文件，不影响其他模块。
3. **可配置性**：区分开发 / 测试 / 生产环境的配置，避免硬编码（如数据库密码、密钥）。

## 二、基础结构：小型项目（个人工具 / Demo）

适用于代码量少（<500 行）、功能单一的项目（如简单 API、个人博客 Demo），结构简洁，无需过度拆分。

### 典型目录结构

```plaintext
your_flask_project/          # 项目根目录
├── app.py                   # 核心入口（集成路由、配置、模型）
├── static/                  # 静态资源（CSS/JS/图片）
│   ├── css/
│   ├── js/
│   └── img/
├── templates/               # 模板文件（HTML，支持Jinja2）
│   ├── index.html
│   └── user.html
├── requirements.txt         # 依赖清单（如Flask、Flask-SQLAlchemy）
└── .gitignore               # Git忽略文件（如venv/、__pycache__/、.env）
```

### 核心文件说明

1. `app.py`

    ：项目入口，集成所有核心逻辑（适合小型项目），示例：

    ```python
    from flask import Flask, render_template
    from flask_sqlalchemy import SQLAlchemy
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # 简单配置
    db = SQLAlchemy(app)
    
    # 模型（小型项目可放此处）
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50))
    
    # 路由（小型项目可放此处）
    @app.route('/')
    def index():
        return render_template('index.html')
    
    if __name__ == '__main__':
        app.run(debug=True)
    ```

2. **`static/`**：存放前端静态资源，模板中通过 `url_for('static', filename='css/style.css')` 引用。

3. **`templates/`**：存放 HTML 模板，支持模板继承（如 `base.html` 作为父模板，其他页面继承）。

4. **`requirements.txt`**：记录依赖，通过 `pip freeze > requirements.txt` 生成，他人通过 `pip install -r requirements.txt` 安装依赖。

## 三、进阶结构：中大型项目（团队协作 / 生产级应用）

当项目涉及多模块（如用户、商品、订单）、多人协作或需要部署到生产环境时，需采用 “包级结构”，将代码拆分为独立子模块，符合 Python 包的规范。

### 典型目录结构（推荐）



```plaintext
your_flask_project/          # 项目根目录
├── app/                     # 核心应用包（所有业务逻辑在此）
│   ├── __init__.py          # 包初始化（创建Flask实例、注册扩展）
│   ├── config.py            # 配置文件（区分环境）
│   ├── models/              # 数据模型（与数据库交互）
│   │   ├── __init__.py
│   │   ├── user.py          # 用户模型
│   │   └── product.py       # 商品模型
│   ├── routes/              # 路由蓝图（按模块拆分）
│   │   ├── __init__.py
│   │   ├── user_bp.py       # 用户相关路由（登录/注册）
│   │   └── product_bp.py    # 商品相关路由（列表/详情）
│   ├── services/            # 业务逻辑层（复杂逻辑抽离）
│   │   ├── __init__.py
│   │   ├── user_service.py  # 用户业务（如密码加密、权限校验）
│   │   └── order_service.py # 订单业务（如创建订单、计算价格）
│   ├── static/              # 静态资源（同基础结构）
│   └── templates/           # 模板文件（同基础结构）
├── migrations/              # 数据库迁移文件（Flask-Migrate生成）
├── tests/                   # 单元测试/集成测试
│   ├── __init__.py
│   ├── test_user.py
│   └── test_product.py
├── .env                     # 环境变量（敏感信息，不提交Git）
├── .env.example             # 环境变量示例（提交Git，指导他人配置）
├── .gitignore
├── requirements.txt
└── run.py                   # 项目启动入口（不包含业务逻辑）
```

### 各模块核心作用与实现（关键代码示例）

#### 1. 入口文件：`run.py`（仅负责启动，不写业务）

避免在入口文件中写复杂逻辑，保持简洁：

```python
from app import create_app  # 从app包的__init__.py导入创建实例的函数

app = create_app()  # 根据环境自动加载配置

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

#### 2. 应用初始化：`app/__init__.py`（核心胶水层）

通过 **工厂函数（`create_app`）** 创建 Flask 实例，实现 “延迟初始化”（便于扩展、测试），并注册蓝图、扩展（如 SQLAlchemy、Migrate）：



```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import config  # 导入配置字典
from app.routes.user_bp import user_bp  # 导入用户蓝图
from app.routes.product_bp import product_bp  # 导入商品蓝图

# 初始化扩展（不绑定app，延迟到create_app时绑定）
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='development'):  # 默认开发环境
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # 加载对应环境的配置

    # 绑定扩展到app
    db.init_app(app)
    migrate.init_app(app, db)

    # 注册蓝图（路由分组）
    app.register_blueprint(user_bp, url_prefix='/user')  # 所有用户路由前缀为/user
    app.register_blueprint(product_bp, url_prefix='/product')  # 商品路由前缀为/product

    return app
```

#### 3. 配置管理：`app/config.py`（区分环境）

将开发、测试、生产环境的配置分开，避免硬编码；敏感信息（如数据库密码）通过 `.env` 文件加载：

```python
import os
from dotenv import load_dotenv  # 需要安装python-dotenv：pip install python-dotenv

# 加载.env文件中的环境变量
load_dotenv()

# 基础配置（所有环境通用）
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_secret_key')  # 从.env获取，默认开发密钥
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 关闭修改跟踪，提高性能

# 开发环境配置（本地开发，调试模式开启）
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI', 'sqlite:///dev.db')

# 测试环境配置（自动化测试，独立数据库）
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI', 'sqlite:///test.db')

# 生产环境配置（线上环境，调试关闭，使用MySQL/PostgreSQL）
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI', 'mysql+pymysql://user:pass@host/db')

# 配置字典，便于通过create_app传入环境名加载
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

#### 4. 环境变量：`.env`（敏感信息，不提交 Git）

存放数据库密码、密钥等敏感信息，通过 `python-dotenv` 加载到 `config.py` 中：

```env
# .env 文件内容（不提交Git）
SECRET_KEY=your_production_secret_key_123
DEV_DATABASE_URI=mysql+pymysql://root:123456@localhost/dev_db
TEST_DATABASE_URI=mysql+pymysql://root:123456@localhost/test_db
PROD_DATABASE_URI=mysql+pymysql://prod_user:prod_pass@prod_host/prod_db
```

#### 5. 模型层：`app/models/`（数据结构定义）

按业务模块拆分模型（如 `user.py`、`product.py`），仅定义数据结构和简单方法，复杂逻辑放 `services/`：

```python
# app/models/user.py
from app import db  # 从__init__.py导入已初始化的db

class User(db.Model):
    __tablename__ = 'users'  # 数据库表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)  # 存储加密后的密码

    # 简单方法：设置密码（加密逻辑可抽离到service）
    def set_password(self, password):
        from werkzeug.security import generate_password_hash  # 密码加密库
        self.password_hash = generate_password_hash(password)

    # 简单方法：验证密码
    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)
```

#### 6. 路由层：`app/routes/`（蓝图拆分，路由分组）

按业务模块创建蓝图（Blueprint），避免所有路由堆在 `app.py`，示例 `user_bp.py`：

```python
# app/routes/user_bp.py
from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db
from app.services.user_service import get_user_by_username  # 调用业务逻辑

# 创建蓝图，名称为'user_bp'
user_bp = Blueprint('user_bp', __name__)

# 路由1：用户注册（POST请求）
@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # 调用service层逻辑（复杂校验放service）
    if get_user_by_username(username):
        return jsonify({'error': 'Username already exists'}), 400

    # 创建用户
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

# 路由2：用户登录（POST请求）
@user_bp.route('/login', methods=['POST'])
def login():
    # 逻辑类似，省略...
    pass
```

#### 7. 业务逻辑层：`app/services/`（复杂逻辑抽离）

将路由中复杂的业务逻辑（如权限校验、数据处理、第三方接口调用）抽离到 `services/`，避免路由层臃肿，示例 `user_service.py`：

```python
# app/services/user_service.py
from app.models.user import User

# 业务逻辑：根据用户名查询用户
def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

# 业务逻辑：批量查询用户（带分页）
def get_users(page=1, per_page=10):
    return User.query.paginate(page=page, per_page=per_page, error_out=False)

# 业务逻辑：用户权限校验（示例）
def check_user_permission(user_id, required_role):
    # 假设User模型有role字段，复杂权限逻辑可在此实现
    user = User.query.get(user_id)
    if not user or user.role != required_role:
        return False
    return True
```

#### 8. 测试层：`tests/`（保证代码稳定性）

按模块编写测试用例，使用 `pytest` 或 Flask 自带的 `unittest`，示例 `test_user.py`：



```python
# tests/test_user.py
import json
import pytest
from app import create_app, db
from app.models.user import User

#  fixtures：测试前创建临时app和数据库
@pytest.fixture
def client():
    app = create_app('testing')  # 使用测试环境配置
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():  # 激活Flask上下文
            db.create_all()  # 创建测试数据库表
            yield client
            db.drop_all()  # 测试后删除表

# 测试用户注册接口
def test_user_register(client):
    response = client.post(
        '/user/register',
        data=json.dumps({'username': 'testuser', 'email': 'test@example.com', 'password': '123456'}),
        content_type='application/json'
    )
    assert response.status_code == 201
    assert json.loads(response.data)['message'] == 'User created successfully'
```

## 四、最佳实践与避坑指南

1. **不要忽略 `__init__.py`**：
    - Python 3.3+ 支持 “命名空间包”，但显式创建空的 `__init__.py`（或包含包初始化逻辑）能确保模块被正确识别，避免导入错误。
2. **敏感信息不提交 Git**：
    - 务必在 `.gitignore` 中加入 `.env`、`venv/`、`*.db`（SQLite 数据库文件），防止密钥、密码泄露。
    - 提供 `.env.example` 作为示例，指导团队成员配置环境变量。
3. **使用蓝图拆分路由**：
    - 当路由超过 10 个时，必须按业务模块拆分蓝图（如 `/user`、`/product`、`/order`），便于维护和权限控制。
4. **业务逻辑与路由分离**：
    - 路由层仅负责 “接收请求、返回响应”，复杂逻辑（如数据校验、数据库事务、第三方调用）全部放 `services/`，便于测试和复用。
5. **环境配置区分清晰**：
    - 开发环境开启 `DEBUG=True`，生产环境必须关闭；测试环境使用独立数据库，避免污染开发 / 生产数据。
6. **使用 Flask-Migrate 管理数据库**：
    - 中大型项目中，严禁手动修改数据库表结构，通过 `flask db migrate` 生成迁移脚本，`flask db upgrade` 执行迁移，确保版本可控。

## 五、扩展：更大规模项目的优化（企业级）

如果项目规模进一步扩大（如百人团队、微服务架构），可在上述结构基础上增加以下优化：

1. **引入 `Flask-RESTful` 或 `FastAPI`**：若为 API 项目，`Flask-RESTful` 可更规范地管理 API 资源，`FastAPI` 则支持异步和自动生成接口文档。
2. **分层更细**：新增 `utils/`（工具函数，如日期处理、加密）、`schemas/`（数据校验，使用 `marshmallow`）、`middlewares/`（中间件，如日志、跨域）。
3. **微服务拆分**：将用户、商品、订单拆分为独立的 Flask 服务，通过 API 网关（如 Nginx、Kong）整合。
4. **使用容器化**：通过 `Docker` 打包项目，`Docker Compose` 管理多服务（如 Flask 应用、MySQL、Redis），确保环境一致性。





























