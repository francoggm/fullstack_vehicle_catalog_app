from flask import request, jsonify, Blueprint, make_response
from werkzeug.utils import secure_filename
from base64 import b64encode

from .models import Vehicle
from .token import token_required
from . import db

routes = Blueprint('routes', __name__)

@routes.route('/vehicle', methods=['GET'])
def get_all_vehicles():
    try:
        vehicles = Vehicle.query.all()
        if vehicles:
            output = [
                {
                    "name": vehicle.name, "brand": vehicle.brand, "model": vehicle.model, "price": vehicle.price, "mileage": vehicle.mileage, "register": vehicle.show_register_date, "format_price": vehicle.show_price, "format_mileage":vehicle.show_mileage, "format_register_date":vehicle.show_register_date, "image": b64encode(vehicle.img).decode('utf-8'),"id": vehicle.id
                } for vehicle in vehicles
            ]
            return jsonify({"vehicles": output}), 200
        return jsonify({"message": "Error getting all vehicles, no vehicle found"}), 404
    except:
        return jsonify({"message": "Error getting all vehicles, try again"}), 400

@routes.route('/vehicle/<id>', methods=['GET'])
def get_vehicle(id):
    try:
        vehicle = Vehicle.query.get(int(id))
        if vehicle:
            return jsonify({
                "vehicle": {
                    "name": vehicle.name, "brand": vehicle.brand, "model": vehicle.model, "price": vehicle.price, "mileage": vehicle.mileage, "register": vehicle.show_register_date, "format_price": vehicle.show_price, "format_mileage":vehicle.show_mileage, "format_register_date":vehicle.show_register_date, "image": b64encode(vehicle.img).decode('utf-8'),"id": vehicle.id
                }
            }), 200
        return jsonify({"message": "Error getting vehicle, no vehicle found"}), 404
    except:
        return jsonify({"message": "Error getting vehicle, try again"}), 400

@routes.route('/vehicle', methods=['POST'])
@token_required
def register_vehicle(current_user):
    try:
        if not current_user or not current_user.admin:
            return jsonify({"message": "You do not have permission to do that"}), 401
        
        picture = request.files.get('file')
        name = request.form.get('name')
        brand = request.form.get('brand')
        model = request.form.get('model')
        price = request.form.get('price')
        mileage = request.form.get('mileage')
        img_name = secure_filename(picture.filename)
        img = picture.read()
        mimetype = picture.mimetype
        if name and brand and model and price and mileage and picture:
            vehicle = Vehicle(name = name, brand = brand, model = model, price = int(price), mileage = int(mileage), img=img, img_name=img_name, mimetype=mimetype)
            db.session.add(vehicle)
            db.session.commit()
            return jsonify({"message": "Vehicle has been added"}), 200
        return jsonify({"message": "Error creating vehicle, missing some informations"}), 400
    except:
        return jsonify({"message": "Error creating vehicle, try again"}), 400

@routes.route('/vehicle/<id>', methods=['PUT'])
@token_required
def update_vehicle(current_user, id):
    try:
        if not current_user or not current_user.admin:
            return jsonify({"message": "You do not have permission to do that"}), 401

        picture = request.files.get('file')
        name = request.form.get('name')
        brand = request.form.get('brand')
        model = request.form.get('model')
        price = request.form.get('price')
        mileage = request.form.get('mileage')
        vehicle = Vehicle.query.get(int(id))
        if vehicle:
            if name and brand and model and price and mileage:
                vehicle.name = name
                vehicle.brand = brand
                vehicle.model = model
                vehicle.price = int(price)
                vehicle.mileage = int(mileage)
                if picture:
                    img_name = secure_filename(picture.filename)
                    img = picture.read()
                    mimetype = picture.mimetype
                    vehicle.img = img
                    vehicle.img_name = img_name
                    vehicle.mimetype = mimetype
                db.session.commit()
                return make_response(jsonify({"message": "Vehicle has been updated"}), 200)
            return make_response(jsonify({"message": "Error updating vehicle, missing some informations"}), 400)
        return make_response(jsonify({"message": "Error updating vehicle, no vehicle found"}), 400)
    except:
        return make_response(jsonify({"message": "Error updating vehicle, try again"}), 400)

@routes.route('/vehicle/<id>', methods=['DELETE'])
@token_required
def delete_vehicle(current_user, id):
    try:
        if not current_user or not current_user.admin:
            return jsonify({"message": "You do not have permission to do that"}), 401

        vehicle = Vehicle.query.get(int(id))
        if vehicle:
            db.session.delete(vehicle)
            db.session.commit()
            return jsonify({"message": "Vehicle has been deleted"}), 200
        return jsonify({"message": "Error deleting vehicle, vehicle not found"}), 404
    except:
        return jsonify({"message": "Error deleting vehicle, try again"}), 400

@routes.route('/vehicle', methods=['DELETE'])
@token_required
def delete_all_vehicles(current_user):
    try:
        if not current_user or not current_user.admin:
            return jsonify({"message": "You do not have permission to do that"}), 401

        vehicles = Vehicle.query.all()
        if vehicles:
            for vehicle in vehicles:
                db.session.delete(vehicle)
            db.session.commit()
            return jsonify({"message": "All vehicles has been deleted"}), 200
        return jsonify({"message": "Error deleting all vehicles, no vehicle registered"}), 404
    except:
        return jsonify({"message": "Error deleting all vehicles, try again"}), 400