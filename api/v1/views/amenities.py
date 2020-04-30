#!/usr/bin/python3
"""the state view"""

from flask import jsonify, request, abort
from api.v1.views import app_views
import models
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', strict_slashes=False, methods=['GET'])
@app_views.route('/amenities/<amenity_id>',
                 strict_slashes=False, methods=['GET'])
def get_amenities(amenity_id=None):
    if amenity_id:
        the_amenity = storage.get(Amenity, amenity_id)
        if the_amenity:
            return (jsonify(the_amenity.to_dict()))
        abort(404)
    else:
        l_amenity = storage.all(Amenity).values()
        lj_amenity = []
        for obj in l_amenity:
            lj_amenity.append(obj.to_dict())
        return (jsonify(lj_amenity))


@app_views.route('/amenities/<amenity_id>', strict_slashes=False,
                 methods=['DELETE'])
def del_amenities(amenity_id):
    the_amenity = storage.get(Amenity, amenity_id)
    if the_amenity:
        storage.delete(the_amenity)
        storage.save()
        return(jsonify({}), 200)
    abort(404)


@app_views.route('/amenities', strict_slashes=False, methods=['POST'])
def post_amenities():
    srjson = request.get_json()
    if srjson:
        if "name" in srjson:
            new_amenity = Amenity(**srjson)
            new_amenity.save()
            return(jsonify(new_amenity.to_dict()), 201)
        else:
            return(jsonify(error="Missing name"), 400)
    else:
        return(jsonify(error="Not a JSON"), 400)


@app_views.route('/amenities/<amenity_id>',
                 strict_slashes=False, methods=['PUT'])
def put_amenities(state_id):
    srjson = request.get_json()
    if srjson:
        if "id" in srjson:
            srjson.pop("id")
        if "created_at" in srjson:
            srjson.pop("created_at")
        if "updated_at" in srjson:
            srjson.pop("updated_at")
        the_amenity = storage.get(Amenity, amenity_id)
        if the_amenity:
            for key, value in srjson.items():
                setattr(the_amenity, key, value)
            the_amenity.save()
            return(jsonify(the_state.to_dict()), 200)
        else:
            abort(404)
    else:
        return(jsonify(error="Not a JSON"), 400)
