class Student:
    def __init__(self, firstName, lastName, fullName):
        self.firstName = firstName 
        self.lastName = lastName 
        self.fullName = fullName
        print(self)
    
s1 = Student("Sandy", "Bhai", "Sandy Bhai")
print(s1.firstName, s1.fullName)
print(s1)
    
    

