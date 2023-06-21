from flask import Flask, jsonify, Blueprint, request
from DAO import SemesterDAO
from datetime import date
from entities.Semester import Semester

app = Flask(__name__)
semesters_bp = Blueprint('semesters', __name__)


def list_semester_serializer(semester):
    return {
        'name': semester[0],
        'beginning_date': semester[1].isoformat() if isinstance(semester[1], date) else None,
        'ending_date': semester[2].isoformat() if isinstance(semester[2], date) else None
    }


def semester_serializer(semester):
    return {
        'name': semester.name,
        'beginning_date': semester.beginning_date.isoformat() if isinstance(semester.beginning_date, date) else None,
        'ending_date': semester.ending_date.isoformat() if isinstance(semester.ending_date, date) else None
    }


@semesters_bp.route('/semesters', methods=['GET'])
def get_semesters():
    semesters = SemesterDAO.getAllSemesters()
    try:
        if semesters:
            serialized_semesters = [list_semester_serializer(semester) for semester in semesters]
            return jsonify({"data": serialized_semesters}), 200
        return jsonify({"message": "No content"}), 204
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500


@semesters_bp.route('/semesters/<name>', methods=['GET'])
def get_semester(name):
    semester = SemesterDAO.getOneSemester(name)
    if semester:
        serialized_semester = semester_serializer(semester)
        print(serialized_semester)
        return jsonify({"data": serialized_semester}), 200
    return jsonify({"message": "semester not found"}), 500


@semesters_bp.route('/semesters', methods=['POST'])
def create_semester():
    data = request.get_json()
    new_semester = Semester(data['name'], data['beginning_date'], data['ending_date'])
    try:
        SemesterDAO.insertSemester(new_semester)
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "Semester created successfully"}), 200


@semesters_bp.route('/semesters/<name>', methods=['PUT'])
def update_semester(name):
    data = request.get_json()
    new_semester = Semester(data['name'], data['beginning_date'], data['ending_date'])
    try:
        SemesterDAO.updateSemester(name, new_semester)
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "Semester updated successfully"}), 200


@semesters_bp.route('/semesters/<name>', methods=['DELETE'])
def delete_semester(name):
    try:
        SemesterDAO.deleteSemester(name)
    except Exception as e:
        return jsonify({"message": "an error has occurred: " + str(e)}), 500
    return jsonify({"message": "Semester deleted successfully"}), 200
