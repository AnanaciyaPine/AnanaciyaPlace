class Student:
    def __init__(self, height=160):
        self.height = height
        print("Hi!I am alive!!!:D")
        print
Dmitro = Student()
print(Dmitro.height)
Katya = Student(height=175)
print(Katya.height)
