# -*- coding: utf-8 -*-
# @Time : 2021/10/23 11:52 上午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :

from applications.extensions import ma
from marshmallow import fields



class TokenPoolSchema(ma.Schema):
    min = fields.Integer()
    max = fields.Integer()
    type = fields.Boolean()
    market_value = fields.Integer()
    circulation = fields.Integer()
    subscribe = fields.Integer()
    unlock = fields.Str()
    start_at = fields.DateTime()
    end_at = fields.DateTime()
    create_at = fields.DateTime()

    class Meta:
        fields = ["min", "max", "type", "market_value", "circulation",
                  "subscribe", "unlock", "start_at","end_at","create_at"]
        ordered = True  # 转换成有序字典