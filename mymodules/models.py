class Student:
    def __init__(self, student_name, student_grade):
        self.student_name=student_name
        self.student_grade=student_grade

    def setGrade(self,grade):
        self.student_grade=grade

    def getGrade(self):
        return self.student_grade

    def printStudentInfo(self):
        print(f"{self.student_name}, {self.student_grade}")
