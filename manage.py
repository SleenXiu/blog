# coding=utf-8
# !/usr/bin/env python
# manage.py 启动程序文件


# import
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models import User, Role, Post


# 创建应用
# app = create_app(os.getenv('BLOG_CONFIG') or 'default')
app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
