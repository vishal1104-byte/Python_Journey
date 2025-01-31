'''
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
'''

'''
There are Two types of Function in python : 1. Built-in function   2. User defined function 
* Built-in function : These function are predefined and pre coded in python   Ex: min(),max(),len(),range(),sum(),type(),print(),dict(),set(),tuple(),set()
* User Defined function : We can create a function to perform specific tasks as per our need .  by using def keyword
'''

# def funct():      # def is the keyword to create the function 
#     print("My name is Vishal")

# funct()          # Calling a function 

# def calculateGmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)
# calculateGmean(8,9)
# calculateGmean(10,12)
# calculateGmean(7,8)


# def greater(a,b):
#     if a>b:
#         print("a is greater")
#     else:
#         print("b is greater")
# greater(10,20)
#                                            Function Arguments 
'''
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.


There are Four Types of argument that we can provide to a function 
1. Default Argument
2. Keyword Argument
3. variable length Argument 
4. Required Argument
'''

# def fun(fname,lname):
#     print(f"My name is {fname} {lname}")
# fun("Vishal","Tiwari")

# def add(a,b):
#     print("The Sum of a and b is ",a+b)
# add(15,85)

#                                            Default Arguments
# We can provide a default value while creating a function . Here function assumes the default value that given in the function if the value is not given 

# def name(fname="Vishal",lname = "Tiwari"):
#     print(f"My full name is {fname} {lname}")
# name("sahil","singh")


#                                            Required Arguments 
# In this case we dont pass the key value syntax , so it is necessary to pass the argument in the correct order 
# Here we have to provide the full argument if we taking three things in function then we have to call all three function that we given over there 

# def name(fname,mname,lname):
#     print(f"My full name is {fname} {mname} {lname}")

# name("Vishal","Dinesh","Tiwari")

#                                              Variable length Arguments

# When I take the function by using (*numbers) it will work as the type tuple
# WHen I take the function by using (**numbers) it will work as the type dictionary

# This is for one star before the function name 
# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("The Average of the Numbers is ",sum / len(numbers))

# average(7,8,9,7,10)

# This is for two star before the function name 
# def fullname(**name):
#     print("My full name is ",name["fname"] ,name["mname"] , name["lname"])

# fullname(fname = "Vishal" , mname = "Dinesh" , lname = "Tiwari")



#                                            Arbitary Arguments , *Args
'''
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly
'''

# def function(*kids):
#     print(f"I have three Child The Youngest name is {kids[1]} and the smallest is {kids[2]}")
# function("Abhay","shivam","Piyush")


#                                          Keyword Arguments ,
''' You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.'''

# def child(child1,child2,child3):
#     print(f"The Youngest child is {child2} and the eldest child is {child3}")
# child(child1 = "Shivam",child2 = "Shivam",child3 = "piyush")

#                                          Default parameters Value 
#If we call the function without argument, it uses the default value:
# def funct(country = "India"):
#     print("I am from ", country)
# funct()
# funct("Pakistan")                        # Yes I can change the default parameter by overwriting the function whe calling 


#                                         Lambda Function
#A lambda function in Python is a small, anonymous function defined using the lambda keyword. It is often used for short-term, throwaway tasks where defining a full function is unnecessary.

# square = lambda x : x**2
# print("The Square of 5 is ",square(5))


#                           POLYMORPHISM :
# Polymorphism is the ability of an object to take on multiple forms. This can be achieved   .  In short ek cheez anek kaam 