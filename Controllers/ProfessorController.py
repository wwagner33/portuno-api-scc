from flask import Flask, jsonify, Blueprint, request
from DAO import ProfessorDAO, UserDAO
from entities.Professor import Professor
from entities.User import User

app = Flask(__name__)
professor_bp = Blueprint('professors', __name__)


@professor_bp.route('/professors', methods=['GET'])
def get_professors():
    users = ProfessorDAO.getAllProfessors()
    try:
        if users:
            serialized_users = [user.__dict__ for user in users]
            return jsonify({"data": serialized_users}), 200
        return jsonify({"message": "No content"}), 204
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500


@professor_bp.route('/professors/<id>', methods=['GET'])
def get_professor(id):
    user = ProfessorDAO.getOneProfessor(id)
    if user:
        serialized_user = user.__dict__
        return jsonify({"data": serialized_user}), 200
    return jsonify({"message": "Professor not found"}), 500

# Ainda precisa ajustar
@professor_bp.route('/professors', methods=['POST'])
def create_professor():
    data = request.get_json()
    new_professor = User(data['id'], data['name'], data['password'], data['ddd'], data['number'])
    try:
        UserDAO.insertUser(new_professor)
        ProfessorDAO.insertProfessor(Professor(data['id']))
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "Professor created successfully"}), 200
