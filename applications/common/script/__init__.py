# -*- coding: utf-8 -*-
# @Time : 2021/10/22 4:38 下午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :
import click
from werkzeug.security import generate_password_hash

from applications.extensions import db
from applications.models import User


def init_script(app):
    @app.cli.command()
    @click.option('--name', prompt="请输入用户名", help='新增用户名')
    @click.option('--password', prompt="请输入密码", help='新增密码')
    def createuser(name, password):
        user = User()
        user.login = name
        user.password = generate_password_hash(password)
        db.session.add(user)
        db.session.commit()