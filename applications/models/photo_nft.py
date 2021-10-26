# -*- coding: utf-8 -*-
# @Time : 2021/10/21 4:18 下午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :

import datetime
from applications.extensions import db


class PhotoNft(db.Model):
    __tablename__ = 'photo_nft'
    id = db.Column(db.Integer, primary_key=True)
    token_id = db.Column(db.Integer,comment="序号")
    rare = db.Column(db.String(255), comment='稀有度')
    name = db.Column(db.String(255), nullable=False, comment="名字")
    discriblem = db.Column(db.String(255), nullable=False, comment="描述")
    href = db.Column(db.String(255), comment="图片路径")
    is_use = db.Column(db.Boolean,comment="是否使用过")
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment="创建时间")