#!/usr/bin/python3
"""doc"""
from api.v1.views import app_views 
from flask import jsonify

@app_views.route("/status")
def statues():
    return jsonify("{'status': 'OK'}")