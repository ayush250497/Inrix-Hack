import flask
from flask_cors import CORS, cross_origin
from app import app
from flask import request

from service.parking import ParkingService


# @app.after_request
# def add_header(response):
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers["Access-Control-Allow-Credentials"] = True
#     return response

CORS(app, support_credentials=True)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/parking')
@cross_origin(supports_credentials=True)
def parking_lots():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    parking_service = ParkingService()
    parking_lots = parking_service.get_parking_lots(longitude=longitude, latitude=latitude)
    print(parking_lots)
    return flask.jsonify(parking_lots)
