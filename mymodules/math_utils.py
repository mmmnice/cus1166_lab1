from mymodules.models import Student
def average_Grade(roster):

    sum=0
    len(roster)
    for i in range(len(roster)):
        sum=sum+roster[i].getGrade()

    return sum/len(roster)
