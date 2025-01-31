# 1.arithmetic arithmatic 

# +    --> This is used for addition
# -    --> This is used for subtraction
# *    --> This is used for multiplication
# /    --> This is used for Division
# %    -->  module operator it is used for  giving the reminder 
# **   -->  multiplying operator
# //   --> dividing operator


# 2. Comparison Operators 

# == equals to 
# <= less than equals 
# >= greater than equals 
# != not equals to 


#  3. Assignment Operators 

# a += 11   SO here 11 will be added after the value of a 
# a -= 11   So here 11 will be subtracted after the value of a 
# a *= 11   So here 11 will be multiply by the previously value of a 

# 4.  Logical Operators :- Operates on the bollena value 

# bool1 = "True"
# bool2 = "False"
# print("The Value of bool1 and bool2 is ",(bool1 and bool2))
# print("The Value of bool1 and bool2 is ",(bool1 or bool2))
# print("The Value of not  bool2 is ",( not bool2))






#                 Arithmetic and Math 

# Math Function 

# x = 3.14
# y = -8
# z = 4

# result = round(x)              # This is round function of math which give the floor value of the number 
# print(result)
# abs = abs(y)
# print(abs)                     # This function will give you the absolute value of the number 
# power = pow(2,4)               # This is the power function which is used at the power number 2 to the power 4 
# print(power)
# print(max(x,y,z))              # This is the max function which is used to select the maximum number from the option 
# print(min(x,y,z))              # This is the min function which is used to select the minimum number from the option 


# There are many more math module 

# import math
# print(math.pi)
# print(math.sqrt(8))            # This function will give you the square root of the Number
# print(math.ceil(3.14))         # This will give you the last number of the point like 4
# print(math.floor(3.14))        # This will give you the least number of the point like 3


# Exercise 
#1 calculate the circumference of a circle 

# import math
# radius = float(input("Enter the radius of a circle: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference of a circle is {round(circumference , 2)}")

#2 calculate the area of a circle 

# import math 
# radius = float(input("Enter the radius of a circle: "))
# area = math.pi * pow(radius,2)
# print(f"The area of a circle is {round(area)}")

#3 calculate the Hypothenus of a triangle 

import math
side1 = float(input("Enter the One Side"))
side2 = float(input("Enter the Second Side"))

hypo = math.sqrt(pow(side1,2) + pow(side2,2))
print(f"The Hypothenus of the square is {round(hypo,2)}cm 😂")    # To add emoji press wind + .