#!/usr/bin/python3
"""
Status of our Api and some stats.
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def app_status():
    """
    Simply returns the state of the api.
    """
    return(jsonify(status="OK"))

<<<<<<< HEAD

@app_views.route("/api/v1/stats")
=======
@app_views.route("/stats")
>>>>>>> ac1f1de30f90f025f559e9d8e01089ecb912830b
def stats():
    """
    Returns statistics about the number of objects available.
    """
    total = {"amenities": storage.count("Amenity"),
             "cities": storage.count("City"),
             "places": storage.count("Place"),
             "reviews": storage.count("Review"),
             "states": storage.count("State"),
             "users": storage.count("User")}
    return jsonify(total)
