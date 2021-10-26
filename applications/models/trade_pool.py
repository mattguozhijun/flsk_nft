# -*- coding: utf-8 -*-
# @Time : 2021/10/22 10:30 上午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :

import datetime
from applications.extensions import db

class TradePool(db.Model):
    __tablename__ = 'trade_pool'
    id = db.Column(db.Integer, primary_key=True)
    ico_id = db.Column(db.Integer, db.ForeignKey("inital_digital_offering.id"), comment='ico主键')
    min = db.Column(db.Integer,  comment='最小认购额')
    max = db.Column(db.Integer,  comment='最大认购额')
    type = db.Column(db.String(20), comment='认购类型（public/private）')
    market_value = db.Column(db.Integer, comment='市值')
    circulation = db.Column(db.Integer, comment='开盘流通量')
    subscribe = db.Column(db.Integer, comment='总认购额')
    unlock = db.Column(db.Text, comment='解锁规则')
    start_at = db.Column(db.DateTime, default=datetime.datetime.now, comment="开始时间")
    end_at = db.Column(db.DateTime, default=datetime.datetime.now, comment="结束时间")
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment="创建时间")