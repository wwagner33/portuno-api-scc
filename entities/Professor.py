from entities.User import User


class Professor(User):
    def __init__(self, user_id, name, password, ddd, number):
        super().__init__(user_id, name, password, ddd, number)
        self._professor_permissions = []

    @property
    def professor_permissions(self):
        return self._professor_permissions

    def add_professor_permission(self, permission):
        self._professor_permissions.append(permission)

    def remove_professor_permission(self, permission):
        self._professor_permissions.remove(permission)

    def get_professor_permission(self, index):
        return self._professor_permissions[index]
