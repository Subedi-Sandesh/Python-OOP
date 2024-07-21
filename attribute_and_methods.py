class Student:
    college_name = "WRC"
    name = "anonymous"#class attribute

    def __init__(self, name, marks):
        self.name = name #obj attribute > class attribute
        self.marks = marks
        print("adding new student in database")

    def greet(self):
        print(f"Hello {self.name} ")

    def get_marks(self):
        return self.marks

s1 = Student("Sandy","98")
s1.greet()
print(s1.name)
print(s1.college_name)
print(s1.get_marks())