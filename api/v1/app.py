#!/usr/bin/python3
""" Web Flask App """
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import jsonify


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(response):
    """ For Teardown """
    storage.close()


@app.errorhandler(404)
def p_n_f(error):
    """ Returns a 404 error 'page'. """
    return jsonify({'error': 'Not found'}), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
