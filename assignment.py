class Assignment:
    def __init__(self, pointsEarned, pointsTotal, assignmentWeight, assignmentCategory):
        self.pointsEarned = pointsEarned
        self.pointsTotal = pointsTotal
        self.assignmentWeight = assignmentWeight
        self.assignmentCategory = assignmentCategory
        self.next = None
    
    def changePointsEarned(self,input):
        self.pointsEarned = input

    def changePointsTotal(self,input):
        self.pointsTotal = input

    def changeAssignmentWeight(self,input):
        self.assignmentWeight = input

    def changeAssignmentCategory(self,input):
        self.assignmentCategory = input

class AssignmentList:
    def __init__(self):
        self.head = None

    def addAssignment(self, assignment):
        if self.head is None:
            self.head = assignment
            return

        current = self.head
        
        while current.next:
            current = current.next
        current.next = assignment


