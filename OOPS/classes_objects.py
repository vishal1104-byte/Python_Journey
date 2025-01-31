# class Person:                              # This is Class 
#     name = "Vishal"
#     occupation = "Software Developer"
#     Networth = '20$'
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a = Person()                               # This is Object 
# b = Person()
# a.occupation = "Manager"                  # This is how we can change the name of the objects 
# a.name = "Vishal"
# # print(a.name)
# # print(a.occupation)
# b.occupation = "Secretary"
# b.name = "Khushbu"
# a.info()
# b.info()



# Self :-->  The self parameter is a reference to the current instances of the class , and is used to access variables that bolongs to the class 

# This is the Proper Example where we use classes and Objects 
class school:
    subject = "science"
    Teacher = "Raksha"
    def info(self):
        print(f"The Subject {self.subject} is teached by {self.Teacher} Teacher")

    
a = school()
b = school()
c = school()
a.subject = "Science"
a.Teacher = "Raksha"
b.subject = "Maths"
b.Teacher = "Rahul"
c.subject = "IT"
c.Teacher = "Vishal"

a.info()
b.info()
c.info()