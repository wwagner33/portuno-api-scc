class Permission:
    def __init__(self, permission_id, beginning_time, ending_time, classroom, user, professor):
        self.id = permission_id
        self.beginning_time = beginning_time
        self.ending_time = ending_time
        self.classroom = classroom
        self.user = user
        self.professor = professor

