# -*- coding: utf-8 -*-
# @Time : 2021/10/20 8:57 下午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :
import os

from flask import Flask

from applications.common.script import init_script
from applications.configs import config
from applications.extensions import init_plugs
from applications.view import init_view


def create_app(config_name=None):
    app = Flask(__name__)
    if not config_name:
        # 尝试从本地环境中读取
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app.config.from_object(config[config_name])

    # 注册各种插件
    init_plugs(app)

    # 注册路由
    init_view(app)

    # 注册命令
    init_script(app)

    return app