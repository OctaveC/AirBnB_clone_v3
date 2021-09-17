#!/usr/bin/python3
""" index.py """
from flask import Flask
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """ Status of API returning JSON """
    ok = {"status": "OK"}
    return jsonify(ok)
