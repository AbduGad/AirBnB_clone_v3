#!/usr/bin/python3
"""doc"""
from flask import Flask
from models import storage
from api.v1.views import app_views 
from flask import jsonify
from flask import Response
from os import getenv

"""doc"""

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()
    
@app.errorhandler(404) 
def not_found(e): 
    return  jsonify({"error": "Not found"}),404

if __name__ == "__main__":
    # app.run(debug=True,host="0.0.0.0",port=5000,threaded=True)
    if getenv("HBNB_API_HOST") is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT") is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(getenv("HBNB_API_PORT"))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)

