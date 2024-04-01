#!/usr/bin/python3
"""main app file for Flask instance in REST API
"""
from api.v1.views import app_views
from flask import Flask,  jsonify
from os import environ
from models import storage
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_storage(exception=None):
    """Close the storage when the app context is torn down."""
    storage.close()

# Custom 404 error handler


@app.errorhandler(404)
def not_found(error):
    """Handle 404 (Not Found) errors."""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    if environ.get("HBNB_API_HOST") is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = environ.get("HBNB_API_HOST")
    if environ.get("HBNB_API_PORT") is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(environ.get("HBNB_API_PORT"))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
