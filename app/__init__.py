from flask import Flask
from flask_googlemaps import GoogleMaps
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

GoogleMaps(app)

from app import routes

