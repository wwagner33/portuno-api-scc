from flask import Flask
from flask_cors import CORS
from flask_session import Session
from Controllers import UserController, SemesterController, \
    SchoolClassController, ClassroomController, ProfessorController, \
    OccupancyController, PermissionController

app = Flask(__name__)
app.register_blueprint(UserController.users_bp)
app.register_blueprint(SemesterController.semesters_bp)
app.register_blueprint(SchoolClassController.school_class_bp)
app.register_blueprint(ClassroomController.classroom_bp)
app.register_blueprint(ProfessorController.professor_bp)
app.register_blueprint(OccupancyController.occupancy_bp)
app.register_blueprint(PermissionController.permission_bp)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

if __name__ == '__main__':
    app.env = 'development'
    app.run()
