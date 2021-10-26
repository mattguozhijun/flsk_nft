# -*- coding: utf-8 -*-
# @Time : 2021/10/20 9:06 下午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :
import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from applications.extensions import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    login = db.Column(db.String(20), comment='用户名')
    remark = db.Column(db.String(255), comment='备注')
    password = db.Column(db.String(128), comment='哈希密码')
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username
