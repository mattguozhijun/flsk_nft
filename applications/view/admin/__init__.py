# -*- coding: utf-8 -*-
# @Time : 2021/10/20 9:03 下午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :
from flask import Flask
from flask_admin.contrib.sqla import ModelView
from flask_babelex import Babel

from applications.extensions import db
from applications.models import User, Trade, PhotoNft, IntalDigitalOffering, Token, TradePool
import flask_admin as admin
from applications.view.admin.passport import MyAdminIndexView
from flask_admin.contrib import sqla
import flask_login as login
from flask import url_for, redirect, request

# Create customized model view class
class BaseModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))

class UserModelView(BaseModelView):
    column_labels = {
        'login': u'用户名',
        'remark': u'备注',
        'password': u'密码',
        'create_at': u'创建时间',
        'update_at': u'更新时间',
    }

class TradeModelView(BaseModelView):
    column_labels = {
        'trade_address': u'交易地址',
        'client_address': u'用户地址',
        'amount': u'数量',
        'item': u'项目',
        'is_use': u'是否有效',
        'is_transfer': u'是否转账',
        'create_at': u'创建时间',
    }

class PhotoNftModelView(BaseModelView):
    column_labels = {
        'token_id': u'序号',
        'rare': u'用户地址',
        'amount': u'名字',
        'name': u'描述',
        'discriblem': u'图片路径',
        'href': u'图片路径',
        'is_use': u'是否使用过',
        'create_at': u'创建时间',
    }

class IntalDigitalOfferingModelView(BaseModelView):
    column_labels = {
        'name': u'项目名',
        'token_id': u'代币名',
        'logo': u'图标',
        'introduce': u'打新项目简介',
        'about': u'关于项目',
        'deadline': u'截止时间',
        'all_amount': u'总数量',
        'current_amount': u'当前认购数量',
        'people_all_amount': u'总参与人数',
        'people_current_amount': u'当前参与人数',
        'token': u'代币',
        'create_at': u'创建时间',
    }

class TokenModelView(BaseModelView):
    column_labels = {
        'name': u'代币名',
        'symbol': u'代币符号',
        'precision': u'小数点',
        'address': u'地址',
        'hardtop': u'总量',
        'ppt_url': u'路演ppt',
        'invest_img': u'投资方展示（图片路径）',
        'create_at': u'创建时间',
    }


class TradePoolModelView(BaseModelView):
    column_labels = {
        'ico_id': u'打新',
        'min': u'最小认购额',
        'max': u'最大认购额',
        'type': u'认购类型（public/private）',
        'market_value': u'市值',
        'circulation': u'开盘流通量',
        'subscribe': u'总认购额',
        'unlock': u'解锁规则',
        'start_at': u'开始时间',
        'end_at': u'结束时间',
        'ido': u'打新',
        'create_at': u'创建时间',
    }

def register_admin_view(app: Flask):
    _admin = admin.Admin(app, name='gamefi_club', index_view=MyAdminIndexView(),
                         template_mode='bootstrap3', base_template='my_master.html',)


    _admin.add_view(UserModelView(User, db.session, name=u'用户'))
    _admin.add_view(TradeModelView(Trade, db.session, name=u'交易记录'))
    _admin.add_view(PhotoNftModelView(PhotoNft, db.session, name="nft图片"))
    _admin.add_view(IntalDigitalOfferingModelView(IntalDigitalOffering, db.session, name="打新"))
    _admin.add_view(TokenModelView(Token, db.session, name="代币"))
    _admin.add_view(TradePoolModelView(TradePool, db.session, name="交易池"))

    # 汉化
    babel = Babel(app)
    app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'