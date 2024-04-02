#!/usr/bin/python3
"""doc"""
from api.v1.views import app_views 
from flask import jsonify
from models import storage
from models import city, place,amenity,review,state,user
@app_views.route("/status")
def statues():
    return jsonify({"status": "OK"})

@app_views.route("/stats")
def stats():
    """return count of class from the database"""
    cls_count_dict={
  "amenities": storage.count(amenity) ,
  "cities": storage.count(city) ,
  "places": storage.count(place)  ,
  "reviews": storage.count(review) ,
  "states":  storage.count(state) ,
  "users":  storage.count(user),
  
}
    return jsonify(cls_count_dict)