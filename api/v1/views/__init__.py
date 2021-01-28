#!/usr/bin/python3
"""
blueprint
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
<<<<<<< HEAD
from api.v1.views.cities import *
=======
from api.v1.views.states import *
>>>>>>> ac1f1de30f90f025f559e9d8e01089ecb912830b
