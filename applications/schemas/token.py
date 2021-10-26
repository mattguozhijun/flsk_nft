# -*- coding: utf-8 -*-
# @Time : 2021/10/23 11:52 上午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :

from applications.extensions import  ma
from marshmallow import fields



class TokenSchema(ma.Schema):
    name = fields.Str()
    symbol = fields.Str()
    precision = fields.Integer()
    address = fields.Str()
    hardtop = fields.Str()
    ppt_url = fields.Str()
    invest_img = fields.Str()
    create_at = fields.DateTime()

    class Meta:
        fields = ["name", "symbol", "precision", "address", "hardtop",
                  "ppt_url", "invest_img", "create_at"]
        ordered = True  # 转换成有序字典