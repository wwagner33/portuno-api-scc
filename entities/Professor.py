from entities.User import User


class Professor(User):
    def __init__(self):
        self.professor_permissions = []

    def add_professor_permission(self, permission):
        self.professor_permissions.append(permission)

    def remove_professor_permission(self, permission):
        self.professor_permissions.remove(permission)

    def get_professor_permission(self, index):
        return self.professor_permissions[index]
