''' # type() function :- This function is used to find the data type of a given variable in python
a = 35
b = "Vishal"
print(type(a))          # It will give class int 
print(type(b))          # It will give class str  '''




'''
Typecasting :-  Typecasting means to converting the one data types into another data types 
A number can be converted into strings and vice versa 
Ex, str(31)   --> "31"  Integer to string     ||     float(32)  --> 32.0   integer to float
'''



'''
input() function :- This function allows the users to take input from the keyboard as a string 

a = input("Enter Your Name")

Note that the output of input is always a string(even if the number is entered)!
But if you want to take number as a input so do this 
a = int(input("Enter the Number ))
'''

# Exercise : 

# Calculate the area of Rectangle 

# length = int(input("Enter the Length of the Rectangle: "))
# width = int(input("Enter the Width of the Rectangle: "))
# area = length * width
# print("The area of the Rectangle is ",area)

#2. Shopping cart Program 
item = input("What item would you like to Buy ? : ")
price = float(input("Enter the Price ? : "))
quantity = int(input("How many would you like to Buy ? :"))

total = price * quantity

print(f"The Total amount You have to pay for {item} is {total}")