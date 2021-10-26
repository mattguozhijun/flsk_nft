# -*- coding: utf-8 -*-
# @Time : 2021/10/20 10:25 下午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :
import datetime

from applications.extensions import db

class Trade(db.Model):
    __tablename__ = 'Trade'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='交易id')
    trade_address = db.Column(db.String(255), comment='交易地址')
    client_address = db.Column(db.String(255), comment='用户地址')
    amount = db.Column(db.Integer, comment='数量')
    item = db.Column(db.String(255), comment='项目')
    is_use = db.Column(db.Boolean, comment='是否有效')
    is_transfer = db.Column(db.Boolean, comment='是否转账')
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
