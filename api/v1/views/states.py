#!/usr/bin/python3
from flask import abort,Flask
from api.v1.views import app_views
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import jsonify
@app_views.route('/states', methods=['GET'])
def get_states():
    cls_dict=storage.all()
    all_states = [cls.to_dict() for id , cls in cls_dict.items()]
    

    return jsonify(all_states)

