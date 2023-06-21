class Occupancy:
    def __init__(self, occupancy_id, beginning_date_time, ending_date_time, goal, classroom, user, semester, the_class):
        self.id = occupancy_id
        self.beginning_time = beginning_date_time
        self.ending_time = ending_date_time
        self.goal = goal
        self.classroom = classroom
        self.user = user
        self.semester = semester
        self.the_class = the_class
