from flask import Flask, jsonify, Blueprint, request
from DAO import ClassroomDAO
from entities.Classroom import Classroom

app = Flask(__name__)
classroom_bp = Blueprint('classrooms', __name__)


@classroom_bp.route('/classrooms', methods=['GET'])
def get_classrooms():
    classrooms = ClassroomDAO.getAllClassrooms()
    try:
        if classrooms:
            serialized_classrooms = [classroom.__dict__ for classroom in classrooms]
            return jsonify({"data": serialized_classrooms}), 200
        return jsonify({"message": "No content"}), 204
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500


@classroom_bp.route('/classrooms/<id>', methods=['GET'])
def get_classroom(id):
    classroom = ClassroomDAO.getOneClassroom(id)
    if classroom:
        serialized_classroom = classroom.__dict__
        return jsonify({"data": serialized_classroom}), 200
    return jsonify({"message": "classroom not found"}), 404


@classroom_bp.route('/classrooms', methods=['POST'])
def create_classroom():
    data = request.get_json()
    print(data)
    new_classroom = Classroom(data['id'], data['name'], data['short_name'], data['floor'], data['type'], data['professor_user_id'])
    try:
        ClassroomDAO.insertClassroom(new_classroom)
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "classroom created successfully"}), 200


@classroom_bp.route('/classrooms/<id>', methods=['PUT'])
def update_classroom(id):
    data = request.get_json()
    new_classroom = Classroom(data['id'], data['name'], data['short_name'], data['floor'], data['type'], data['professor_user_id'])
    try:
        ClassroomDAO.updateClassroom(id, new_classroom)
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "classroom updated successfully"}), 200


@classroom_bp.route('/classrooms/<id>', methods=['DELETE'])
def delete_classroom(id):
    try:
        ClassroomDAO.deleteClassroom(id)
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "classroom deleted successfully"}), 200
