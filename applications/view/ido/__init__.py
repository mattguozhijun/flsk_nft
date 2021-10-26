# -*- coding: utf-8 -*-
# @Time : 2021/10/23 10:38 上午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :

from flask import Blueprint, request, jsonify

from applications.common import validate, contract, curd
from applications.common.contract import validate_trade
from applications.common.http import success_api, fail_api
from applications.models import IntalDigitalOffering
from applications.schemas import IntalDigitalOfferingSchema

ido_bp = Blueprint('api_ido', __name__, url_prefix='/ido')


def register_ido_views(app):
    app.register_blueprint(ido_bp)


@ido_bp.get('/list')
def list():
    ido = IntalDigitalOffering.query.all()
    print(ido)
    res = {
        "data": curd.model_to_dicts(schema=IntalDigitalOfferingSchema,data=ido),
        "status": {"code": 200}
    }
    return jsonify(res)


@ido_bp.get('/<int:_id>')
def get(_id):
    ido = curd.get_one_by_id(IntalDigitalOffering, _id)
    print(ido)
    res = {
        "data": curd.model_to_dicts(schema=IntalDigitalOfferingSchema,data=ido,many=False),
        "status": {"code": 200}
    }
    return jsonify(res)