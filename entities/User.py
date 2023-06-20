class User:
    def __init__(self, id, name, password, ddd, number):
        self.id = id
        self.name = name
        self.password = password
        self.ddd = ddd
        self.number = number
        self.permissions = []
        self.occupancies = []

    def add_permission(self, permission):
        self.permissions.append(permission)

    def remove_permission(self, permission):
        self.permissions.remove(permission)

    def get_permission(self, index):
        return self.permissions[index]

    def add_occupancy(self, occupancy):
        self.occupancies.append(occupancy)

    def remove_occupancy(self, occupancy):
        self.occupancies.remove(occupancy)

    def get_occupancy(self, index):
        return self.occupancies[index]
