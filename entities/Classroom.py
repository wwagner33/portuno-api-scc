class Classroom(object):

    def __init__(self, id, name, short_name, floor, type):
        self.type = type
        self.floor = floor
        self.short_name = short_name
        self.name = name
        self.id = id
