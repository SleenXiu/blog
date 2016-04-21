# coding=utf-8
# created by sleen 

from flask import render_template, request
from . import main
from flask_login import current_user, login_required
from ..decorators import admin_required, permission_required
from ..models import Permission

@main.route('/')
def index():
    show_followed = False
    if current_user.is_authenticated:
        show_followed = bool(request.cookies.get('show_followed', ''))
    return render_template('index.html',show_followed=show_followed)


@main.route('/admin')
@login_required
@admin_required
def for_admin_only():
    return "For administrators!"