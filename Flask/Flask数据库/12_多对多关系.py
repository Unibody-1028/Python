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