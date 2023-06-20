class SchoolClass:
    def __init__(self, class_id, day_week, subject):
        self._id = class_id
        self._day_week = day_week
        self._subject = subject
        self._occupancies = []

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def day_week(self):
        return self._day_week

    @day_week.setter
    def day_week(self, new_day_week):
        self._day_week = new_day_week

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, new_subject):
        self._subject = new_subject

    @property
    def occupancies(self):
        return self._occupancies

    def add_occupancy(self, occupancy):
        self._occupancies.append(occupancy)

    def remove_occupancy(self, occupancy):
        self._occupancies.remove(occupancy)

    def get_occupancy(self, index):
        return self._occupancies[index]
