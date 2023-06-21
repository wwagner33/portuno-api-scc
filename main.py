from flask import Flask
from Controllers import UserController, SemesterController, SchoolClassController, ClassroomController

app = Flask(__name__)
app.register_blueprint(UserController.users_bp)
app.register_blueprint(SemesterController.semesters_bp)
app.register_blueprint(SchoolClassController.school_class_bp)
app.register_blueprint(ClassroomController.classroom_bp)

if __name__ == '__main__':
    app.env = 'development'
    app.run()
