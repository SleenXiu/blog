# coding=utf-8
# created by sleen 
# auth/__init__.py 认证蓝本

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views


