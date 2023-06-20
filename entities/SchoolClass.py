class SchoolClass:
    def __init__(self, class_id, day_week, subject):
        self.id = class_id
        self.day_week = day_week
        self.subject = subject
        self.occupancies = []

    def add_occupancy(self, occupancy):
        self.occupancies.append(occupancy)

    def remove_occupancy(self, occupancy):
        self.occupancies.remove(occupancy)

    def get_occupancy(self, index):
        return self.occupancies[index]
