#!usr/bin/python3
"""Blueprints and routes"""
from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')

from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.states import *
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_review import *
