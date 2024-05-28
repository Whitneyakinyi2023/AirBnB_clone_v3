#!/usr/bin/python3
"""
Initialization file for v1"""

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='api/v1')

from ap1.v1.views.index import *