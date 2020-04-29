#!usr/bin/python3
"""methods for app_views"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def status():
    """return the status"""
    return jsonify({'status': 'OK'}), 200
