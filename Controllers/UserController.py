from flask import Flask, jsonify, Blueprint
from DAO import UserDAO

app = Flask(__name__)
users_bp = Blueprint('users', __name__)


@users_bp.route('/users', methods=['GET'])
def get_users():
    users = UserDAO.getAllUsers()
    serialized_users = [user.__dict__ for user in users]
    print(users)
    return jsonify({"data": serialized_users})


@users_bp.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = UserDAO.getUserById(id)
    if user is None:
        return jsonify({'message': 'Usuário não encontrado'}), 404
    return jsonify({'data': user.__dict__})


@users_bp.route('/users', methods=['POST'])
def create_user():
    pass


@users_bp.route('/users/<id>', methods=['PUT'])
def update_user(id):
    pass


@users_bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    pass
