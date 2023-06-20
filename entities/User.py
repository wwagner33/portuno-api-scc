class User:
    def __init__(self, user_id, name, password, ddd, number):
        self._id = user_id
        self._name = name
        self._password = password
        self._ddd = ddd
        self._number = number
        self._permissions = []
        self._occupancies = []

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def ddd(self):
        return self._ddd

    @ddd.setter
    def ddd(self, new_ddd):
        self._ddd = new_ddd

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, new_number):
        self._number = new_number

    @property
    def permissions(self):
        return self._permissions

    def add_permission(self, permission):
        self._permissions.append(permission)

    def remove_permission(self, permission):
        self._permissions.remove(permission)

    def get_permission(self, index):
        return self._permissions[index]

    @property
    def occupancies(self):
        return self._occupancies

    def add_occupancy(self, occupancy):
        self._occupancies.append(occupancy)

    def remove_occupancy(self, occupancy):
        self._occupancies.remove(occupancy)

    def get_occupancy(self, index):
        return self._occupancies[index]
