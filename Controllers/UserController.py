from flask import Flask, jsonify, Blueprint, request
from DAO import UserDAO
from entities.User import User

app = Flask(__name__)
users_bp = Blueprint('users', __name__)


@users_bp.route('/users', methods=['GET'])
def get_users():
    users = UserDAO.getAllUsers()
    if users:
        serialized_users = [user.__dict__ for user in users]
        return jsonify({"data": serialized_users}), 200
    return jsonify({"message": "an error has occurred"}), 500


@users_bp.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = UserDAO.getOneUser(id)
    if user:
        serialized_user = user.__dict__
        return jsonify({"data": serialized_user}), 200
    return jsonify({"message": "User not found :("}), 500


@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(data['id'], data['name'], data['password'], data['ddd'], data['number'])
    try:
        UserDAO.insertUser(new_user)
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "User created successfully"}), 200


@users_bp.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    new_user = User(data['id'], data['name'], data['password'], data['ddd'], data['number'])
    try:
        UserDAO.updateUser(id, new_user)
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "User updated successfully"}), 200


@users_bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        UserDAO.deleteUser(id)
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "User deleted successfully"}), 200
