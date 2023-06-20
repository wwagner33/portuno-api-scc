class Semester:
    def __init__(self, name, beginning_date, ending_date):
        self._name = name
        self._beginning_date = beginning_date
        self._ending_date = ending_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def beginning_date(self):
        return self._beginning_date

    @beginning_date.setter
    def beginning_date(self, new_beginning_date):
        self._beginning_date = new_beginning_date

    @property
    def ending_date(self):
        return self._ending_date

    @ending_date.setter
    def ending_date(self, new_ending_date):
        self._ending_date = new_ending_date
