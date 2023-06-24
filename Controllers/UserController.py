from flask import Flask, jsonify, Blueprint, request, session
from DAO import UserDAO
from entities.User import User

app = Flask(__name__)
users_bp = Blueprint('users', __name__)


@users_bp.route('/users', methods=['GET'])
def get_users():
    if 'user_id' in session:
        users = UserDAO.getAllUsers()
        try:
            if users:
                serialized_users = [user.__dict__ for user in users]
                return jsonify({"data": serialized_users}), 200
            return jsonify({"message": "No content"}), 204
        except Exception as e:
            return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "access denied"}), 404


@users_bp.route('/users/<id>', methods=['GET'])
def get_user(id):
    if 'user_id' in session:
        user = UserDAO.getOneUser(id)
        if user:
            serialized_user = user.__dict__
            return jsonify({"data": serialized_user}), 200
        return jsonify({"message": "User not found"}), 500
    return jsonify({"message": "access denied"}), 404


@users_bp.route('/users', methods=['POST'])
def create_user():
    if 'user_id' in session:
        data = request.get_json()
        new_user = User(data['id'], data['name'], data['password'], data['ddd'], data['number'])
        try:
            UserDAO.insertUser(new_user)
        except Exception as e:
            return jsonify({"message": "an error has occurred: " + str(e)}), 500
        return jsonify({"message": "User created successfully"}), 200
    return jsonify({"message": "access denied"}), 404


@users_bp.route('/users/<id>', methods=['PUT'])
def update_user(id):
    if 'user_id' in session:
        data = request.get_json()
        new_user = User(data['id'], data['name'], data['password'], data['ddd'], data['number'])
        try:
            UserDAO.updateUser(id, new_user)
        except Exception as e:
            return jsonify({"message": "an error has occurred: " + str(e)}), 500
        return jsonify({"message": "User updated successfully"}), 200
    return jsonify({"message": "access denied"}), 404


@users_bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    if 'user_id' in session:
        try:
            UserDAO.deleteUser(id)
        except Exception as e:
            return jsonify({"message": "an error has occurred: " + str(e)}), 500
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"message": "access denied"}), 404


@users_bp.route('/auth', methods=['POST'])
def auth():
    authorization = False
    data = request.get_json()
    id = data['id']
    password = str(data['password'])
    user = UserDAO.getOneUser(id)
    if user:
        if user.password == password:
            print("Era pra ficar autorizado")
            authorization = True
    if authorization:
        session['user_id'] = user.id
        session['user_name'] = user.name
        return jsonify({"authorization": True, "user": {"id": user.id, "name": user.name}})
    else:
        session.clear()  # Remove todas as variáveis da sessão
        return jsonify({"authorization": False, "message": "Falha no login"})
