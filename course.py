from assignment import Assignment, AssignmentList

class Course:
    def __init__(self, name):
        self.name = name  # Name of the course
        self.assignments = AssignmentList()

    def add_assignment(self, points_earned, points_total, weight, category):
        new_assignment = Assignment(points_earned, points_total, weight, category)
        self.assignments.add_assignment(new_assignment)