#!/usr/bin/python3
"""Creation of a flask app"""

from api.v1.views import app_views
from flask import jsonify
from flask import Flask
from models import storage

@app_views.route('/status')
def api_status():
    """Method to have a JSON resposne"""
    response = {'status': "OK"}

@app_views.route('/stats')
def get_stats():
    """Returns stratus"""
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }

    return jsonify(stats)

app = Flask(__name__)

app.register_blueprint(app_views)

if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_HOST', 5000))
    app.run(port=PORT, host=HOST, threaded=True)