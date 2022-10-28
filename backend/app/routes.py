from flask import request, jsonify, Blueprint

from .models import Vehicle
from .token import token_required
from . import db

routes = Blueprint('routes', __name__)

@routes.route('/vehicle', methods=['GET'])
def get_all_vehicles():
    try:
        vehicles = Vehicle.query.all()
        if vehicles:
            output = [{"name": vehicle.name, "brand": vehicle.brand, "model": vehicle.model, "price": vehicle.show_price, "mileage": vehicle.show_mileage, "register": vehicle.show_register_date} for vehicle in vehicles]
            return jsonify({"vehicles": output})
        return jsonify({"message": "Error getting all vehicles, no vehicle found"})
    except:
        return jsonify({"message": "Error getting all vehicles, try again"})

@routes.route('/vehicle/<id>', methods=['GET'])
def get_vehicle(id):
    try:
        vehicle = Vehicle.query.get(int(id))
        if vehicle:
            return jsonify({"vehicle": {"name": vehicle.name, "brand": vehicle.brand, "model": vehicle.model, "price": vehicle.show_price, "mileage": vehicle.show_mileage, "register": vehicle.show_register_date}})
        return jsonify({"message": "Error getting vehicle, no vehicle found"})
    except:
        return jsonify({"message": "Error getting vehicle, try again"})

@routes.route('/vehicle', methods=['POST'])
@token_required
def register_vehicle(current_user):
    try:
        if not current_user or not current_user.admin:
            return jsonify({"message": "You do not have permission to do that"})

        data = request.get_json()
        if data.get('name') and data.get('brand') and data.get('model') and data.get('price') and data.get('mileage'):
            vehicle = Vehicle(name = data['name'], brand = data['brand'], model = data['model'], price = data['price'], mileage = data['mileage'])
            db.session.add(vehicle)
            db.session.commit()
            return jsonify({"message": "Vehicle has been added"})
        return jsonify({"message": "Error creating vehicle, missing some informations"})
    except:
        return jsonify({"message": "Error creating vehicle, try again"})

@routes.route('/vehicle/<id>', methods=['PUT'])
@token_required
def update_vehicle(current_user, id):
    try:
        if not current_user or not current_user.admin:
            return jsonify({"message": "You do not have permission to do that"})

        vehicle = Vehicle.query.get(int(id))
        if vehicle:
            data = request.get_json()
            if data.get('name') and data.get('brand') and data.get('model') and data.get('price') and data.get('mileage'):
                vehicle.name = data['name']
                vehicle.brand = data['brand']
                vehicle.model = data['model']
                vehicle.price = data['price']
                vehicle.mileage = data['mileage']
                db.session.commit()
                return jsonify({"message": "Vehicle has been updated"})
            return jsonify({"message": "Error creating vehicle, missing some informations"})
        return jsonify({"message": "Error updating vehicle, no vehicle found"})
    except:
        return jsonify({"message": "Error updating vehicle, try again"})

@routes.route('/vehicle/<id>', methods=['DELETE'])
@token_required
def delete_vehicle(current_user, id):
    try:
        if not current_user or not current_user.admin:
            return jsonify({"message": "You do not have permission to do that"})

        vehicle = Vehicle.query.get(int(id))
        if vehicle:
            db.session.delete(vehicle)
            db.session.commit()
            return jsonify({"message": "Vehicle has been deleted"})
        return jsonify({"message": "Error deleting vehicle, vehicle not found"})
    except:
        return jsonify({"message": "Error deleting vehicle, try again"})

@routes.route('/vehicle', methods=['DELETE'])
@token_required
def delete_all_vehicles(current_user):
    try:
        if not current_user or not current_user.admin:
            return jsonify({"message": "You do not have permission to do that"})

        vehicles = Vehicle.query.all()
        if vehicles:
            for vehicle in vehicles:
                db.session.delete(vehicle)
            db.session.commit()
            return jsonify({"message": "All vehicles has been deleted"}) 
        return jsonify({"message": "Error deleting all vehicles, no vehicle registered"})
    except:
        return jsonify({"message": "Error deleting all vehicles, try again"})