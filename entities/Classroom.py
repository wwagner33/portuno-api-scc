class Classroom(object):

    def __init__(self, id, name, short_name, floor, type):
        self._type = type
        self._floor = floor
        self._short_name = short_name
        self._name = name
        self._id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def short_name(self):
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        self._short_name = short_name

    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, floor):
        self._floor = floor

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

