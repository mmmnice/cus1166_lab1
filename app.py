from mymodules.models import Student
from mymodules.math_utils import average_Grade


class main():
    StudentList = []

    StudentList.append(Student("Raymond", 90))
    StudentList.append(Student("James", 75))
    StudentList.append(Student("Michelle", 47))
    StudentList.append(Student("Jack", 86))
    StudentList.append(Student("Paul", 79))
    StudentList.append(Student("Jackie", 37))
    StudentList.append(Student("Marie", 84))
    StudentList.append(Student("Doug", 45))
    StudentList.append(Student("Dan", 65))
    StudentList.append(Student("Chris", 99))


    for i in range(len(StudentList)):
        StudentList[i].printStudentInfo()


    print(f"Average Class Score: {average_Grade(StudentList)}")
