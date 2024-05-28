#!/usr/bin/python3
"""Status of your API"""

from ap1.v1.views import app_views
from flask import Flask
from models import storage

app = Flask(__name__)

app.register_blueprint(app_views)


if __name__ == '__main__':
    HOST = getenv()
    PORT = int(getenv())
    app.run(host=HOST, port=PORT, threaded=True)
