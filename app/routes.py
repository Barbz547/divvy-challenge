from app import app, db
from flask import jsonify, request
from app.models import Trip
from datetime import datetime


@app.route('/' , methods=['GET'])
def home():
    return "hello world!"

@app.route('/user', methods=['GET'])
def get_user():
    return jsonify([u.to_dict() for u in Trip.query.all()])

@app.route('/user/<int:trip_id>', methods=['GET'])
def get_users(trip_id):
    return jsonify(Trip.query.get(trip_id).to_dict())

@app.route('/start/<string:starttime>', methods=['GET'])
def get_time(starttime):
    starttimed = datetime.strptime(starttime, "%m/%d/%y %H:%M")
    return jsonify(Trip.query.get(starttimed).to_dict())

    


