# -*- coding: utf-8 -*-
# @Time : 2021/10/21 4:12 下午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :
from flask import Blueprint, request

from applications.common import validate,contract
from applications.common.contract import validate_trade
from applications.common.http import success_api, fail_api

trade_bp = Blueprint('api_trade', __name__, url_prefix='/trade')


def register_trade_view(app):
    app.register_blueprint(trade_bp)



@trade_bp.post('/save')
def save():
    req = request.json
    item = validate.xss_escape(req.get("item"))
    trade_address = contract.toChecksumAddress(validate.xss_escape(req.get("trade_address")))
    if trade_address is None:
        return fail_api(msg="合约地址有误")
    else:
        if validate_trade(trade_address, item):
            return success_api(msg="成功")
        else:
            return fail_api(msg="失败")

