#!/usr/bin/python
""" Module for City related endpoints"""
from api.v1.views import app_views
from flask import jsonify, make_response, abort, request
from models import storage
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities', strict_slashes=False,
                 methods=["GET"])
def get_cities(state_id):
    """city information for all cities"""
    t_state = storage.get("State", state_id)
    if t_state is None:
        abort(404)
    cities = []
    for city in t_state.cities:
        cities.append(city.to_dict())
    return jsonify(cities)


@app_views.route("/cities/<city_id>", strict_slashes=False,
                 methods=["GET"])
def get_city(city_id):
    """city information """
    t_city = storage.get("City", city_id)
    if t_city is None:
        abort(404)
    return jsonify(t_city.to_dict())


@app_views.route("/cities/<city_id>", strict_slashes=False,
                 methods=["DELETE"])
def delete_city(city_id):
    """ Deletes a city id """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    return (jsonify({}))


@app_views.route("/api/v1/states/<state_id>/cities", strict_slashes=False,
                 methods=["POST"])
def post_city(state_id):
    state_js = storage_get("State", state_id)
    if state_js is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    d_arg = request.get_json()
    d_arg['state_id'] = state_id
    city = City(**d_arg)
    city.save()
    return make_response(jsonify(city.to_dict()), 201)


@app_views.route('/cities/<string:city_id>', methods=['PUT'],
                 strict_slashes=False)
def put_city(city_id):
    """update a city"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(city, attr, val)
    city.save()
    return jsonify(city.to_dict())
