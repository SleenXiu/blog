# coding=utf-8
# created by sleen
# main/__init__.py 认证蓝本

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views



