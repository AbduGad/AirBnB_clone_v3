from flask import Blueprint
from flask import url_for
app_views=Blueprint("app_views",__name__,url_prefix="/api/v1")
from api.v1.views.index  import *
