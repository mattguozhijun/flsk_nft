# -*- coding: utf-8 -*-
# @Time : 2021/10/20 9:23 下午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :


# Create customized index view class that handles login & registration
from flask import url_for, redirect, request, Flask
from flask_admin import helpers, expose

from applications.extensions import db
from applications.models import User
import flask_admin as admin
import flask_login as login
from wtforms import form, fields, validators
from werkzeug.security import generate_password_hash, check_password_hash


class LoginForm(form.Form):
    login = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('用户不存在')

        if not check_password_hash(user.password, self.password.data):

            raise validators.ValidationError('密码错误')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()





class MyAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = ''
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()


    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))

    @expose('/<path:path>')
    def get_dir(self, path):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()