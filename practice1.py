# class Student:
#     def __init__(self, name, m1, m2, m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def avg(self):
#         print(f"Average of {self.m1,self.m2,self.m3} of {self.name} is {(self.m1+self.m2+self.m3)/3}")

# s1 = Student("Sandy",56,54,50)
# s1.avg()


#GOOD PRACTICE IS TO PASS THE MARKS AS THE LIST

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum+= val
        print(f"Hi {self.name}. Your average marks is {sum/3}")


s1 = Student("Sandy",[56,57,59])
s1.get_avg()




