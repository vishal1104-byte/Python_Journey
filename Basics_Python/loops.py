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

# Decremental While loop
# count = 5
# while count > 0:
#     print(count)
#     count = count - 1

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
For Loops is used to execute a block of code for a fixed number of time 
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


'''
Nested Loops --> A loop within another loop (outer or inner )
outer loop : Outside the loop 
inner loop : Inside the Loop 
'''

# for x in range(3):
#     for y in range(1,11):     
#         print(y,end=" ")                # This is inner loop 
#     print()                             # This is outer loop 


# for i in range(3):
#     for j in range(5):
#         print("*",end="")
        
#     print()

# Creating the pattern of 1 star than 2 star than as follow
# rows = 6
# for i in range(1,rows+1):
#     print("*" * i)
    

# Write a Multiplication table of the number which is given by the user 
# num = int(input("Enter the Number to get the table of that number "))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")

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




# Question on Loops ?

# 1. Given a list of Numbers , count how many are positive 
# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
# Positive_Numbers = 0
# for num in numbers:
#     if num > 0:
#         Positive_Numbers = Positive_Numbers + 1
#         print(num)
# print("The Total Number of Positive Numbers in the list are ", Positive_Numbers)    
      
# 2. Calculate the sum of Even numbers upto a given number n .

# num = int(input("Enter the Number: "))
# sum_Even = 0
# for i in range(1,num+1):
#     if i%2==0:
#         sum_Even += i
#         print(i)
# print("The Summation of Even Number is ",sum_Even)


# 3. Print the Multiplication table for a given number up to 10 , but skip the fifth iteration 

# num = int(input("Enter the Number to get the table of that number: "))
# for i in range(1,11):
#     if i == 5:
#         continue
#     print(f"{num} X {i} = {num*i}")

# 4. Reverse a string using the Loops 

# str = "Vishal is the Best Person in the World"
# reversed_str = ""
# for char in str:
#     reversed_str = char + reversed_str 
# print(reversed_str)

# 5. Reverse a sentence using the loops 
# sentence = input("Enter Whatever in your mind ")
# words = sentence.split()
# reversed_words = ""
# for word in reversed(words):
#     reversed_words += word + " "

# reversed_sentence = reversed_words.strip()
# print(reversed_sentence)

# 6. Given a string find the first non-repeated characters 
# str = input("Enter any string")
# for c in str:
#     counting = str.count(c)
#     if counting == 1:
#         print("The Non Repeated character in the string is ",c)

# factorial of a number ?
# number = int(input("Enter the Number to get the Factorial of that Number: "))
# factorial = 1
# while number > 0:
#     factorial = factorial * number
#     number = number - 1
# print("The Factorial of the Number is ",factorial)

# Validate input 


# while True:
#     num = int(input("Enter any Number: "))
#     if num > 0 and num < 10:
#         print('The Number is Valid') 
#     else:
#         print("The Number is Invalid")   

# Check if the number is prime or not
# num = int(input("Enter the Number: "))
# is_prime = True

# if num > 1:
#     for i in range(2,num):
#         if(num%i)==0:
#             is_prime = False
#             break
# if is_prime:
#     print(num, "is a prime Number ")
# else:
#     print(num, "is not a prime Number ")


# Duplicate checker 

# items = ["apple","banana","orange","apple","mango"]
# unique_item = set()
# for item in items:
#     if item in unique_item:
#         print(item,"is a duplicate item")
#     else:
#         unique_item.add(item)

# Implement the Exponential Backoff staretegy that doubles the wait times between retries , starting from 1 second , but stops after 5 retries 

# import time

# wait_time = 1
# max_retries = 5
# attempts = 0

# while attempts < max_retries:
#     print("attempts",attempts + 1,"- wait time",wait_time,)
#     time.sleep(wait_time)
#     wait_time *= 2
#     attempts += 1
# print("Happy Birthday Vishal")


# Exercises 
#1. Take name as input
# name = input('Enter Your name: ')
# while name == "":
#     print("You didnt written Anything")
#     name = input("Enter Your name: ")
# print(f"Hello {name}")

#2. check age 
# age = int(input("Enter Your age that are you able to do or nto : "))

# while age < 18:
#     print("You are not able to do this You are small")
#     age = int(input("Enter Your age that are you able to do or not : "))

# print("Yess Now You can Do ")

#3. check food
# food = input("Enter the Nasta You like more and press q to quit: ")

# while not food == "q" :
#     print(f"You Like {food}")
#     food = input('Enter another Nashta Name You like and write q to quit: ')
# print("Bye")

# 4. WHile a Number is between 1 to 10 
# num = int(input("Enter the Number between 1 - 10: "))
# while num < 1 or num > 10 :
#     print("You Entered Invalid NUmber ")
#     num = int(input("Enter the Valid Number: "))
# print(f"Okay Finally You entered a Valid Number {num}")



    

