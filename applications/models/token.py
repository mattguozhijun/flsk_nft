# -*- coding: utf-8 -*-
# @Time : 2021/10/22 10:30 上午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :

import datetime
from applications.extensions import db

class Token(db.Model):
    __tablename__ = 'token'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), comment='代币名')
    symbol = db.Column(db.String(50), comment='代币符号')
    precision = db.Column(db.Integer, comment='小数点')
    address = db.Column(db.String(255), comment='地址')
    hardtop = db.Column(db.Integer, comment='总量')
    ppt_url = db.Column(db.String(255), comment='路演ppt')
    invest_img = db.Column(db.String(255), comment='投资方展示（图片路径）')
    # 创建关系属性  relationship("关联的类名", backref="对方表查询关联数据时的属性名")
    ico_id = db.relationship("IntalDigitalOffering", backref="token")
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment="创建时间")

    def __str__(self):
        return self.name