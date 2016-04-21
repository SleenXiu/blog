# coding=utf-8
# created by sleen
# decorators.py 检查用户权限自定义的修饰器


# import
from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_funcation(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_funcation
    return decorator

def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)
