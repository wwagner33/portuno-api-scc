from flask import Flask, jsonify, Blueprint, request
from DAO import SchoolClassDAO
from entities.SchoolClass import SchoolClass

app = Flask(__name__)
school_class_bp = Blueprint('classes', __name__)


@school_class_bp.route('/classes', methods=['GET'])
def get_school_classes():
    school_classes = SchoolClassDAO.getAllSchoolClasses()
    try:
        if school_classes:
            serialized_school_classes = [school_class.__dict__ for school_class in school_classes]
            return jsonify({"data": serialized_school_classes}), 200
        return jsonify({"message": "No content"}), 204
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500


@school_class_bp.route('/classes/<id>', methods=['GET'])
def get_school_class(id):
    school_class = SchoolClassDAO.getOneSchoolClass(id)
    if school_class:
        serialized_school_class = school_class.__dict__
        return jsonify({"data": serialized_school_class}), 200
    return jsonify({"message": "class not found"}), 404


@school_class_bp.route('/classes', methods=['POST'])
def create_school_class():
    data = request.get_json()
    new_school_class = SchoolClass(None, data['day_week'], data['subject'], data['hour'])
    try:
        SchoolClassDAO.insertSchoolClass(new_school_class)
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "class created successfully"}), 200


@school_class_bp.route('/classes/<id>', methods=['PUT'])
def update_school_class(id):
    data = request.get_json()
    new_school_class = SchoolClass(None, data['day_week'], data['subject'], data['hour'])
    try:
        SchoolClassDAO.updateSchoolClass(id, new_school_class)
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "class updated successfully"}), 200


@school_class_bp.route('/classes/<id>', methods=['DELETE'])
def delete_school_class(id):
    try:
        SchoolClassDAO.deleteSchoolClass(id)
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "class deleted successfully"}), 200
