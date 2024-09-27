'''
Iteration is the fancy name of the loops or doing the things again again 

In python, Loops are control structures used to execute a block of code repeatidely until a certain condition is met . They allow you to automate tasks.


Primary there are two types of loops in python 
1. For loops
2. while loops 
'''


'''
While loops is used for undefinite Times !
While Loops ---> A while loop is used to execute a block of statements repeatedely until a given condition is satisfied . And when the condition becomes false , the line immediately after the loops in the programm is executed 
'''
# count = 1
# while count <= 5:
#     print(i)
#     i += 1


# Write a python program to print all the even numbers between 1 and 50 using while loops 
# num = 0
# while num <= 50:
#     if num%2 == 0:
#         print(num)
#     num += 1


# email = input("Enter Your Email Address: ")
# valid_email = False
# while not valid_email:
#     if "@" in email and "." in email:
#         print("Email Adress Validation Passed")
#         valid_email = True
#     else:
#         print("Invalid Email address Format ! Try again")
#         email = input("Enter Your Email adress: ")


'''
For Loops is used for definite Times!
For Loops --->  The for loop in python is indeed used to iterate over sequences such as lists,tuples,strings,dictionaries and ranges . It allows you to execute a block of code for each item in the sequences 
'''

# numbers = [1,2,3,4,5,6,7,8]
# for x in numbers:
#     print(x)

# str = "Students"
# for i in str:
#     print(i) 

# for z in range(1,25):                                 # This is range function in for loops 
#     if z%2 == 0:
#         print("The Number is Even",z)         
#     else:
#         print("The Number is Odd",z)                  # conditions in for loops 



# items = int(input("Enter the Number of Items You purchased: "))
# total_price = 0
# for i in range(items):
#     price = float(input("Enter the Price of the items: "))
#     total_price = total_price + price
#     i = i + 1

    
# if total_price >= 100:
#     print(f"You get 10% discount and you have to pay {total_price -((total_price*10)/100)} rs")
# elif total_price > 50:
#     print(f"You get 5% discount and you have to pay {total_price -((total_price*5)/100)}")
# else:
#     print(f"No discount applicable since you purchase only {total_price} amount so you have to pay full amount")