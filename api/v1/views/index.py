#!/usr/bin/python3
"""
Status of our Api and some stats.
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


classes = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route("/status")
def app_status():
    """
    Simply returns the state of the api.
    """
    return(jsonify(status="OK"))


@app_views.route("/api/v1/stats")
def stats():
    """
    Returns statistics about the number of objects available.
    """
    new_dict = {}
    for key, value in classes.items():
        new_dict[key] = storage.count(value)
    return jsonify(new_dict)
