class Occupancy:
    def __init__(self, occupancy_id, date, beginning_time, ending_time, goal, classroom, user, semester, the_class):
        self._id = occupancy_id
        self._date = date
        self._beginning_time = beginning_time
        self._ending_time = ending_time
        self._goal = goal
        self._classroom = classroom
        self._user = user
        self._semester = semester
        self._the_class = the_class

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        self._date = new_date

    @property
    def beginning_time(self):
        return self._beginning_time

    @beginning_time.setter
    def beginning_time(self, new_beginning_time):
        self._beginning_time = new_beginning_time

    @property
    def ending_time(self):
        return self._ending_time

    @ending_time.setter
    def ending_time(self, new_ending_time):
        self._ending_time = new_ending_time

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, new_goal):
        self._goal = new_goal

    @property
    def classroom(self):
        return self._classroom

    @classroom.setter
    def classroom(self, new_classroom):
        self._classroom = new_classroom

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, new_user):
        self._user = new_user

    @property
    def semester(self):
        return self._semester

    @semester.setter
    def semester(self, new_semester):
        self._semester = new_semester

    @property
    def the_class(self):
        return self._the_class

    @the_class.setter
    def the_class(self, new_the_class):
        self._the_class = new_the_class
