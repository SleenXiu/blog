# coding=utf-8
# created by sleen
# main/__init__.py 认证蓝本

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views
from ..models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)



