'''
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
'''

def funct():      # def is the keyword to create the function 
    print("My name is Vishal")

funct()          # Calling a function 



#                                            Function Arguments 
'''
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
'''

# def fun(fname,lname):
#     print(f"My name is {fname} {lname}")
# fun("Vishal","Tiwari")


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
def funct(country = "India"):
    print("I am from ", country)
funct()
funct("Pakistan")                        # Yes I can change the default parameter by overwriting the function whe calling 


