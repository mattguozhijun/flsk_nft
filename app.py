# -*- coding: utf-8 -*-
# @Time : 2021/10/17 9:10 下午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :


from flask_migrate import Migrate
from applications import create_app
from applications.extensions.init_sqlalchemy import db

app = create_app()

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
