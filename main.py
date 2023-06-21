from flask import Flask
from Controllers import UserController

app = Flask(__name__)

app.register_blueprint(UserController.users_bp)

if __name__ == '__main__':
    app.run()