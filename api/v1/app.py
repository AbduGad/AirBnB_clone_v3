#!/usr/bin/python3
"""doc"""
from flask import Flask
from models import storage
from api.v1.views import app_views 
from api.v1.views import statues
"""doc"""

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()
    
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000,threaded=True)

