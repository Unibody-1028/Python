from flask_shop import create_app,db
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager


app = create_app('develop')

# 初始化命令管理器
manager = Manager(app)
manager.add_command('db',MigrateCommand)

# 初始化迁移工具
migrate = Migrate(app,db)

if __name__ == '__main__':
    app.run(port=app.config['PORT'])
