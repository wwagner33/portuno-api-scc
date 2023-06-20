class Permission:
    def __init__(self, permission_id, beginning_time, ending_time, classroom, user, professor):
        self._id = permission_id
        self._beginning_time = beginning_time
        self._ending_time = ending_time
        self._classroom = classroom
        self._user = user
        self._professor = professor

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

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
    def professor(self):
        return self._professor

    @professor.setter
    def professor(self, new_professor):
        self._professor = new_professor
