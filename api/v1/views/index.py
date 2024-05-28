#!/usr/bin/python3
"""Creation of a flask app"""

from api.v1.views import app_views
from flask import jsonify
from flask import Flask

@app_views.route('/status')
def api_status():
    """Methos to have a JSON resposne"""
    response = {'status': "OK"}

app = Flask(__name__)

app.register_blueprint(app_views)

if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_HOST', 5000))
    app.run(port=PORT, host=HOST, threaded=True)