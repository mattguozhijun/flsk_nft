# -*- coding: utf-8 -*-
# @Time : 2021/10/20 8:59 下午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :
from flask import Flask

from .init_login import init_login_manager
from .init_sqlalchemy import db, ma, init_databases

def init_plugs(app: Flask) -> None:
    init_databases(app)
    init_login_manager(app)


