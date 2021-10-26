# -*- coding: utf-8 -*-
# @Time : 2021/10/23 11:52 上午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :

from applications.extensions import  ma
from marshmallow import fields




class IntalDigitalOfferingSchema(ma.Schema):
    name = fields.Str()
    # token = fields.Method("get_token")
    logo = fields.Str()
    introduce = fields.Str()
    about = fields.Str()
    deadline = fields.DateTime()
    all_amount = fields.Integer()
    current_amount = fields.Integer()
    people_all_amount = fields.Integer()
    people_current_amount = fields.Integer()
    trade_pool_id = fields.List(fields.Nested(
        "TokenPoolSchema",
    ))
    token = fields.Nested(
        "TokenSchema",
    )
    create_at = fields.DateTime()

    # def get_token(self, obj):
    #     if obj.token_id != None:
    #         return Token.query.filter_by(id=obj.token_id).first()
    #     else:
    #         return None

    class Meta:
        fields = ["logo", "introduce", "about", "deadline", "all_amount",
                  "current_amount", "people_all_amount", "people_current_amount","trade_pool_id","token"]
        ordered = True  # 转换成有序字典
