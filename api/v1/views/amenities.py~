#!/usr/bin/python3
"""the state view"""

from flask import jsonify, request, abort
from api.v1.views import app_views
import models
from models import storage
from models.state import State


@app_views.route('/states', strict_slashes=False, methods=['GET'])
@app_views.route('/states/<state_id>', strict_slashes=False, methods=['GET'])
def get_states(state_id=None):
    if state_id:
        the_state = storage.get(State, state_id)
        if the_state:
            return (jsonify(the_state.to_dict()))
        abort(404)
    else:
        l_state = storage.all(State).values()
        lj_state = []
        for obj in l_state:
            lj_state.append(obj.to_dict())
        return (jsonify(lj_state))


@app_views.route('/states/<state_id>', strict_slashes=False,
                 methods=['DELETE'])
def del_states(state_id):
    the_state = storage.get(State, state_id)
    if the_state:
        storage.delete(the_state)
        storage.save()
        return(jsonify({}), 200)
    abort(404)


@app_views.route('/states', strict_slashes=False, methods=['POST'])
def post_states():
    srjson = request.get_json()
    if srjson:
        if "name" in srjson:
            new_state = State(**srjson)
            new_state.save()
            return(jsonify(new_state.to_dict()), 201)
        else:
            return(jsonify(error="Missing name"), 400)
    else:
        return(jsonify(error="Not a JSON"), 400)


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['PUT'])
def put_states(state_id):
    srjson = request.get_json()
    if srjson:
        if "id" in srjson:
            srjson.pop("id")
        if "created_at" in srjson:
            srjson.pop("created_at")
        if "updated_at" in srjson:
            srjson.pop("updated_at")
        the_state = storage.get(State, state_id)
        if the_state:
            for key, value in srjson.items():
                setattr(the_state, key, value)
            the_state.save()
            return(jsonify(the_state.to_dict()), 200)
        else:
            abort(404)
    else:
        return(jsonify(error="Not a JSON"), 400)
