#!/usr/bin/python3
"""Status of your API"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_engine(exception):
    """storage handling"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Jsonified error handler"""
    response = {"error": "Not found"}
    return jsonify(response), 404


if __name__ == '__main__':
    HOST = getenv()
    PORT = int(getenv())
    app.run(host=HOST, port=PORT, threaded=True)
