# -*- coding: utf-8 -*-
# @Time : 2021/10/20 9:03 下午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :


from applications.view.admin import register_admin_view
from applications.view.trade import register_trade_view
from applications.view.ido import register_ido_views


def init_view(app):
    register_admin_view(app)
    register_trade_view(app)
    register_ido_views(app)