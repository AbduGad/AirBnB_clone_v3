#!/usr/bin/python3
"""index file, main view file
"""
from api.v1.views import app_views
from models import storage, amenity , state, place, review, city, user
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def get_status():
    """define the status message"""
    response = {
        "status": "OK"
        }
    return jsonify(response)


@app_views.route('/stats', methods=['GET'])
def get_number_of_objects():
    """A route to count the number of every object type"""
    obj = {
        "amenities": storage.count(amenity.Amenity),
        "cities": storage.count(city.City),
        "places": storage.count(place.Place),
        "reviews": storage.count(review.Review),
        "states": storage.count(state.State),
        "users": storage.count(user.User)
    }
    return jsonify(obj)

if __name__ == "__main__":
    pass
