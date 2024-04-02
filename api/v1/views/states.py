#!/usr/bin/python3
from flask import abort,Flask
from api.v1.views import app_views
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import jsonify
@app_views.route('/states', methods=['GET'])
def get_states():
    x=storage.all()
    for key, value in x.items():
        print(type(key),type(value))
    return "{}"

