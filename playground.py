#py + name of the class to run a module in the command prompt

print("Practicing Basic input")

myName = input("What is your name:")
print("Hello " + str(myName))

print("Hello %s" % myName)

print("These are Variables")
i = 120
print(f"Variable i is {i}")
f = 1.6180339
print(f"variable f has the value {f} and its type is {type(f)}")
b = False
print(f"{b} has the type {type(b)}")


print("Tuples")
a=(10,20,30)
print(f"a[0] has the value {a[0]} and is the type {type(a)}")

print("setting Variables")
v=set()
v.add(1)
v.add(2)
v.add(3)
v.add(4)
print(v)

print("dictionary")
grades = {"Ray" : "A","Randy": "B"}
print(grades["Ray"])
grades["Bob"]= "D"
print(grades["Bob"])

#empty dictionary
mydictionary =dict()

print("Conditionals")
x=10
if (x > 0):
    print(f"The number {x} is positive")
elif (x < 0):
    print(f"The number {x} is negative")
else:
    print(f"The number {x} is 0")

print("loops")
for i in range(5):
    print(i)

for i_idx, i_value in enumerate(range(2,10)):
    print(f"{i_idx}-{i_value}")

print("functions")
x=19
def is_even(x):
    if(x%2)== 0:
        return True
    else:
        return False

print(is_even(x))

class Book:
    def __init__(self, title="Software Engineering", isbn=""):
        self.title=title
        self.isbn =isbn
    def printBook(self):
        print(self.title + ", " + self.isbn)

from helper_utils import square
print("Imported class helper_utils with the square function")


print (square(100))
