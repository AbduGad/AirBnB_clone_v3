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
    #? latency bug fixed
    storage.reload()
    cls_count_dict={
  "amenities": storage.count(amenity.Amenity) ,
  "cities": storage.count(city.City) ,
  "places": storage.count(place.Place)  ,
  "reviews": storage.count(review.Review) ,
  "states":  storage.count(state.State) ,
  "users":  storage.count(user.User),
  
}
    return jsonify(cls_count_dict)