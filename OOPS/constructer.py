#   constructer : A constructor is a special method in a class used to create and initialize an object of a class 

# class person:
#     def __init__(self,n,o):   // This is a Parameterized Constructor        # This is Dunder method of constructor 
#         self.name = n
#         self.occupation = o
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a = person("Vishal","Developer")
# b = person("Payal","Assistant")
# a.info()
# b.info()


# There are Two types of constructor in python 
# 1. Parameterized Constructor --> When an object accept various argument sach as used above self,name,occ etc is an example of parameterized constructor 
# 2. Default Constructor --> When an object doesnt accept any arguments from the object and only one argument self in the constructor   Below is the example 

class Detils:
    def __init__(self):               # This is the Example of Default Constructor 
        print("Animal are best thing in the world ")

obj = Detils()