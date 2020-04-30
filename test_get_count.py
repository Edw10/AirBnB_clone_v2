#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State
from flask import jsonify

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

listo = []
print(storage.all(State).values())
for obj in storage.all(State).values():
    listo.append(obj.to_dict())
print(listo)
first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))
