from flask import Flask, jsonify, request
import db_service, requests


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify('Occupancy service')

# See all occupancy data
@app.route('/occupancy')
def get_occupancy():
    occupancies = db_service.get_occupancies()
    return jsonify(occupancies)

# Create a new occupancy
@app.route('/occupancy', methods=['POST'])
def create_occupancy():
    # Checkout is missing, but should still be a key
    occupancy = request.json
    db_service.create_occupancy(occupancy)
    return jsonify("Occupancy created"), 201

# Update check-out date for an occupancy
@app.route('/occupancy/<int:row_id>', methods=['PATCH'])
def update_occupancy(row_id):
    occupancy = request.json
    db_service.update_occupancy(occupancy, row_id)
    return jsonify("Occupancy updated"), 200


# List all occupied rooms
@app.route('/occupancy/rooms', methods=['GET'])
def get_occupied_rooms():
    occupied = db_service.get_rooms()

    return jsonify(occupied), 200


if __name__ == '__main__':
    db_service.init()  # Ensure the database is initialized before running
    app.run(host='0.0.0.0')