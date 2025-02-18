#1. Create a car class with attribute like brand and model . Then create an instance of this class 

# class Car:
#     def __init__(self,brand,model):           # This init is constructor 
#         self.brand = brand
#         self.model = model

# my_car = Car("Suzuki","Creta")
# print(my_car.brand)      
# print(my_car.model)   

# my_new_car = Car("Toyota","corolla")
# print(my_new_car.brand)
# print(my_new_car.model)

#2. Add a method to the car class that displays the full name of the car (brand , model )

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
# my_car = Car("Mahindra","Thar")
# print(my_car.full_name())

#3. Inheritance : Create an ElectricCar class that inherits from the car class and has an additional attribute battery_size

# class ElectricCar(Car):                  # This is Inheritance which is like the child of the main class Car 
#     def __init__(self, brand , model , battery_size):
#         super().__init__(brand,model)       # This super keyword is used to take the action of upper side method 
#         self.battery_size = battery_size

# my_tesla = ElectricCar("Tesla","Model S","85KW")
# print(my_tesla.model)
# print(my_tesla.full_name())



# Encapsulation is the concept of restricting access to certain details of an objects and only allowing access to those details through public methods (also called getter and setter).  
# The Purpose of Encapsulation is to protect the integrity of the objects data and hide its complexity 
#4. Encapsulation : Modify the car class to encapsulate the brand attribute , making it private , and provide a getter method for it.

# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model

#     def get_brand(self):             # This is the getter method which is used to hide the method and is only accessible by using getter method 
#         return self.__brand + "!"
    
# my_car = Car("Suzuki","creta")
# print(my_car.get_brand())            # This is the way to access the private member in encapsulation
# print(my_car.model)


# 5 : Polymorphism : Polymosphism allows us to use a single interface to reperesent different types of object 
# Demonstrate polymorphism by defining a method fuel_type in both car and electriccar classes, but with different behaviours  


# class Fuelcar:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def fuel_type(self):
#         return "Petrol and Diesel"
    
# class Electriccar:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def fuel_type(self):   # See same method but having different object than fuelcar this is polymorphism
#         return "Electric Charging"
    
# my_Fuelcar = Fuelcar("Tata","Safari")
# my_Electriccar = Electriccar("Tesla","Model S")
# print(my_Fuelcar.fuel_type())
# print(my_Electriccar.fuel_type())

# 6. Class Variable : Add a class variable to car that keeps track of the number of cars created 
# class Car:

#     total_car = 0
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#         Car.total_car += 1

#     def get_details(self,brand,model):
#         return f"Brand : {self.brand} , Model : {self.model}"
    
#     def fuel_type(self):
#          return "Petrol and Diesel"
    
# my_car_detaill = get_details("Tata","Safari")
# print(my_car_detaill)     
# print(Car.total_car)


# 7. Static Method : A Static method in Python is a method that belongs to a class but does not bind to instance of a class
#  Add a static method to the car class that returns a general description of a car 

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     @staticmethod                                       # This is a decorator 
#     def general_description():
#         return "car is a means of transport"
    


# my_car = Car("Tata","Safari")
# print(my_car.full_name())
# print(my_car.general_description())
# print(Car.general_description())


# 8. Property Decorator : Use a property decorator in the Car class to make the model attribute read only .
# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.__model = model                # By putting this __ we private the model 

#     def full_name(self):
#         return f"{self.brand} {self.__model}"
    
#     @staticmethod
#     def general_description():
#         return "car is a means of transport"
    
#     @property                                # This is also the decorator 
#     def model(self):
#         return self.__model
    
# my_car = Car("Tata","Safari")
# # my_car.model = "Nexon"                            # Here We know that we can overwrite the model 
# print(my_car.full_name())
# print(my_car.general_description())
# print(Car.general_description())
# print(my_car.model)

# 9. Class Inheritance and isinstance() Function : Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and Electric car .

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
# class ElectricCar(Car):                  # This is Inheritance which is like the child of the main class Car 
#     def __init__(self, brand , model , battery_size):
#         super().__init__(brand,model)       # This super keyword is used to take the action of upper side method 
#         self.battery_size = battery_size

# my_tesla = ElectricCar("Tesla","Model S","85KW")
# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))

# 10. Multiple Inheritance : Create Two classes Battery and Engine , and let the Electriccar class inherit from both , demonstrating multiple inheritance  


# class Battery:
#     def Battery_Info(self):
#         return "This is Battery"

# class Engine:
#     def Engine_Info(self):
#         return "This is Engine"

# class Electriccar2(Battery,Engine):   # This is how multiple inheritance work in python 
#     pass

# my_newtesla  = Electriccar2()
# print(my_newtesla.Engine_Info())
# print(my_newtesla.Battery_Info())