import datetime

from flask import Flask, jsonify, Blueprint, request
from DAO import ProfessorDAO, UserDAO, PermissionDAO
from entities.Ocupancy import Occupancy
from entities.Permission import Permission
from entities.Professor import Professor
from entities.User import User

app = Flask(__name__)
permission_bp = Blueprint('permissions', __name__)


@permission_bp.route('/permissions', methods=['GET'])
def get_permissions():
    permissions = PermissionDAO.getAllPermissions()
    try:
        if permissions:
            serialized_permissions = [permission.__dict__ for permission in permissions]
            return jsonify({"data": serialized_permissions}), 200
        return jsonify({"message": "No content"}), 204
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500


# GET ALL DATA FROM PERMISSION
@permission_bp.route('/permissions/<id>', methods=['GET'])
def get_permission(id):
    occupancy = PermissionDAO.getOnePermission(id)
    if occupancy:
        serialized_user = occupancy.__dict__
        return jsonify({"data": serialized_user}), 200
    return jsonify({"message": "Permission not found"}), 500


@permission_bp.route('/permissions', methods=['POST'])
def create_permission():
    data = request.get_json()
    new_permission = Permission(None, data['beginning_date_time'], data['ending_date_time'], data['classroom'],
                                data['user'], data['professor'])
    try:
        success = PermissionDAO.insertPermission(new_permission)
        if not success:
            return jsonify({"message": "Not found"}), 404
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "Permission started successfully"}), 200


@permission_bp.route('/permissions/<id>', methods=['PUT'])
def increase_permission(id):
    data = request.get_json()
    try:
        success = PermissionDAO.updatePermission(id, data['ending_date_time'])
        if not success:
            return jsonify({"message": "Not found"}), 404
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "Permission increased successfully"}), 200


@permission_bp.route('/permissions/<id>', methods=['DELETE'])
def delete_permission(id):
    try:
        success = PermissionDAO.deletePermission(id)
        if not success:
            return jsonify({"message": "Not found"}), 404
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "Permission deleted successfully"}), 200
