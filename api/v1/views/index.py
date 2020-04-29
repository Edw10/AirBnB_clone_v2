#!/usr/bin/python3
"""methods for app_views"""

from flask import jsonify
from api.v1.views import app_views
from models.amenities import Amenity
from models.places import Place
from models.cities import City
from models.review import Review
from models.states import State
from models.users import User

@app_views.route("/status")
def status():
    """return the status"""
    return jsonify({'status': 'OK'})

@app_views.route('/stats', methods=["GET"])
def get_stats():
    """"""
    dic = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(dic)
