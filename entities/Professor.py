from entities.User import User


class Professor(User):
    def __init__(self, user_id):
        self.user_id = user_id
