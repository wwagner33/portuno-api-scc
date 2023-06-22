import datetime

from flask import Flask, jsonify, Blueprint, request
from DAO import ProfessorDAO, UserDAO, OccupancyDAO
from entities.Ocupancy import Occupancy
from entities.Professor import Professor
from entities.User import User

app = Flask(__name__)
occupancy_bp = Blueprint('occupancies', __name__)


@occupancy_bp.route('/occupancies', methods=['GET'])
def get_occupancies():
    occupancies = OccupancyDAO.getAllOccupancies()
    try:
        if occupancies:
            serialized_occupancies = [occupancy.__dict__ for occupancy in occupancies]
            return jsonify({"data": serialized_occupancies}), 200
        return jsonify({"message": "No content"}), 204
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500


@occupancy_bp.route('/occupancies/<id>', methods=['GET'])
def get_professor(id):
    occupancy = OccupancyDAO.getOneOccupancy(id)
    if occupancy:
        serialized_user = occupancy.__dict__
        return jsonify({"data": serialized_user}), 200
    return jsonify({"message": "Occupancy not found"}), 500


@occupancy_bp.route('/occupancies', methods=['POST'])
def create_occupancy():
    data = request.get_json()
    new_occupancy = Occupancy(None, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), None, data['goal'],
                              data['classroom'], data['user'], data['semester'], data['class'])
    try:
        success = OccupancyDAO.insertOccupancy(new_occupancy)
        if not success:
            return jsonify({"message": "Not found"}), 404
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "Occupancy started successfully"}), 200


@occupancy_bp.route('/occupancies/<id>', methods=['PUT'])
def finish_occupancy(id):
    new_occupancy = Occupancy(None, None, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), None,
                              None, None, None, None)
    try:
        success = OccupancyDAO.updateOccupancy(id, new_occupancy)
        if not success:
            return jsonify({"message": "Not found"}), 404
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "Occupancy finished successfully"}), 200

@occupancy_bp.route('/occupancies/<id>', methods=['DELETE'])
def delete_occupancy(id):
    try:
        success = OccupancyDAO.deleteOccupancy(id)
        if not success:
            return jsonify({"message": "Not found"}), 404
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "Occupancy deleted successfully"}), 200
