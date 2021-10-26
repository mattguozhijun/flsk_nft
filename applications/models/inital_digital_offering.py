# -*- coding: utf-8 -*-
# @Time : 2021/10/22 10:11 上午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :

import datetime
from applications.extensions import db

class IntalDigitalOffering(db.Model):
    __tablename__ = 'inital_digital_offering'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), comment='项目名')
    token_id = db.Column(db.Integer, db.ForeignKey("token.id"), comment='token主键')
    logo = db.Column(db.String(255), comment='图标')
    introduce = db.Column(db.String(255), comment='打新项目简介')
    about = db.Column(db.String(255), comment='关于项目')
    deadline = db.Column(db.DateTime, default=datetime.datetime.now, comment="截止时间")
    all_amount = db.Column(db.Integer, comment='总数量')
    current_amount = db.Column(db.Integer, comment='当前认购数量')
    people_all_amount = db.Column(db.Integer, comment='总参与人数')
    people_current_amount = db.Column(db.Integer, comment='当前参与人数')
    # 创建关系属性  relationship("关联的类名", backref="对方表查询关联数据时的属性名")
    trade_pool_id = db.relationship("TradePool", backref="ido")
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment="创建时间")

    def __str__(self):
        return self.name