#                                        Question on Variables and Data Types 

# 1. Program to add,subtract,multiply,divide two numbers 
# a = int(input("Enter the First Number: "))
# b = int(input("Enter the Second NUmber: "))
# print("The Sum of Two Numbers is \n",a+b)
# print("The Product of Two Numbers is\n ",a*b)
# print("The Subtraction of Two Numbers is\n",a-b)
# print("The Division of Two Numbers\n",a/b)

# 2. program to find a remainder when a number is divided by Two 
# Number=int(input("Enter The Number "))
# div=int(input("Enter the number of division"))
# remainder=Number%div
# print(f"The Remainder of {Number} is {remainder}")

# # 3. Using comparison Operator Find out whether a given variable a is greater than b or not 
# a=34
# b=63
# if(a<b):
#      print("a is Smaller")
# else:
#      print("a is greater ")

# 4. Write a python program to find out the average of two number given by the user

# a=int(input("Enter the first Number \n"))
# b=int(input("Enter the second Number\n"))
# avg=(a+b)/2
# print("Average of Two Numbers is \n",avg)

# 5. Write a python Program to find out the square and cube  of the Number given by the user 

# num=int(input("Enter the Number to get the Square,cube of that Number\n"))
# sq=num*num
# cu=num*num*num
# print("The Square of ",num,"is",sq)
# print("The Cube of the",num,"is",cu)


#                               Quetions on Strings 

# 1. Write a program to display a user Enterd name followed by Good Afternoon using input function?
# name = input("Enter Your Name: ")
# print(f"Good Afternoon {name}")

# 2.  Write a program to detect Double spacing in strings ?

# def detect_double_space(string):
#     if "  " in string:
#         return True
#     else:
#         return False

# word = input("Enter any Word: ")
# result = detect_double_space(word)

# if result:
#     print("Double space is detected!")
# else:
#     print("DOuble Space is Not detected")


#                           Questions on conditional statements 
# 1. Write a program to find the greatest of four numbers entered by the users 
# num1 = int(input("Enter the First Number:"))
# num2 = int(input("Enter the Second Number:"))
# num3 = int(input("Enter the third Number:"))
# num4 = int(input("Enter the fourth Number:"))

# if num1 > num2 or num1 > num3 or num1 > num4:
#     print(f"{num1} is Greater")
# elif num2 > num1 or num2 > num3 or num2 > num4:
#     print(f"{num2} is Greater")
# elif num3 > num1 or num3 > num2 or num3 > num4:
#     print(f"{num3} is Greater")
# else:
#     print(f"{num4} is Greater")


# 2. Write a Program to find out whether a student is pass or fail , if it requires total 40% and atleast 33% in each subject to pass . Assume 3 subjects and take marks as an input from the user 

# sub1 = int(input("Enter Your marks: "))
# sub2 = int(input("Enter your marks: "))
# sub3 = int(input("Enter your marks: "))

# avg = sum(sub1,sub2,sub3)/300 * 100

# if sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
#     print("Pass")
# elif avg >= 40:
#     print("pass")
# else:
#     print("Fail")


# 3. Age group classification : child(<13),teenager(13-19),adult(20-59),senior(60+)

# print("Lets we see your age Group ")
# name = input("Enter Your Name: ")
# age = int(input("Enter your age: "))
# if age < 13:
#     print(f"{name} your are Child")
# elif age > 13 and age <= 19:
#     print(f"{name} you are Teenager")
# elif age > 19 and age <= 59:
#     print(f"{name} you are Adult")
# else:
#     print(f"{name} you are Senior")


# 4. Movie Ticket Pricing  | Movie ticket are price based on age : 180rs for adults (18 and over ), 120rs for children . Everyone gets a 2% percent discount on wednesday

# print("Hello Everyone ! Today's Movie Ticket Price is 180rs but It it will be less or higher depends on your age ")
# name = input("Enter your name: ")
# age = int(input("Enter Your age: "))
# day = input("Enter Todays Day: ")
# if day == "Wednesday":
#     amt = 180 - ((180*2)/100)
#     print(f"Congratulation! \n you get 2% discount because you are watching movie on Wednesday \n and You have to pay {amt}rs")
# if age < 18 :
#     print("Your Ticket Price is 120rs")
# else:
#     print("Your Ticket price is 180rs")


# 5. Fruit ripeness checker |   Determine if a fruit is ripe , overripe, or unripe based on its color . (eg. Banana: Green-unripe,yellow-ripe,brown-overripe)

# fruit_name = ["Apple","Banana","papaya","Lemon"]
# print(fruit_name)
# fruits_name = input("Enter the Fruit name from the choices")
# fruit_color = input("Enter the Fruit Color: ")
# if fruits_name == fruit_name[0]:
#     if fruit_color == "Green":
#         print("Fruit is unripe")
#     elif fruit_color == "Red":
#         print("Fruit is ripe ")
#     else:
#         print("Fruit is Overipe")

# elif fruits_name == fruit_name[1]:
#     if fruit_color == "Green":
#         print("Fruit is unripe")
#     elif fruit_color == "Yellow":
#         print("Fruit is ripe ")
#     else:
#         print("Fruit is Overipe")

# elif fruits_name == fruit_name[2]:
#     if fruit_color == "Green":
#         print("Fruit is unripe")
#     elif fruit_color == "Yellow":
#         print("Fruit is ripe ")
#     else:
#         print("Fruit is Overipe")

# else:
#     if fruit_color == "Green":
#         print("Fruit is unripe")
#     elif fruit_color == "Yellow":
#         print("Fruit is ripe ")
#     else:
#         print("Fruit is Overipe")


# 6. Weather activity suggestion |  Suggest an actvity based on the weather (e.g. Sunny-Go for Walk,Rainy- read a book,Snowy-Build a snowman )

# inp = input("Hey Hii my Friend tell me todays weather ? sunny,rainy or snowy: ")
# if inp == "sunny":
#     print("Sunny Started Go for a walk ")
# elif inp == "rainy":
#     print("Rainy started Read a book")
# else:
#     print("Snowy started Build a Snowman")


# 7. Transportation mode Selection | choose a mode of transpotation based on the distance (e.g. <3KM : Walk,3-15 KM :Bike,>15KM : car )

# print("Transpotation Mode Selection ")
# dis = int(input("Tell me what is the distance of your Destination in Kilo Meter: "))
# if dis <= 3:
#     mode = "Walk"
# elif dis <= 15:
#     mode = "Bike"
# else:
#     mode = "car"
    
# print(mode)



#                                         Questions on Loops 

#1. Count Positive Numbers | Given a list of numbers , count how many ar positive 

# numbers = [ 1,2,-3,4,-5,6,7,-8,-9,10]
# positive_numbers  = 0
# for x in numbers:
#     if x > 0:
#         positive_numbers = positive_numbers + 1
# print("The Final count of a positive Numbers is ", positive_numbers)


#2 . Sum of Even Numbers  |  calculate the sum of even numbers up to a given number n .

# num = int(input("Enter the Number to get the sum of Even Number: "))
# sum = 0
# for i in range(num+1):
#     if i%2 == 0:
#         sum += 1
#         print(i)


# print(sum)


# start = 1
# end = 10

# if start % 2 != 0:
#     start += 1

# total_sum = 0
# for i in range(start, end + 1, 2):
#     total_sum += i

# print(f"Sum of even numbers from {start} to {end} is: {total_sum}")


#3. Multiplication Table Printer |  Print a multiplication table for a given number upto 10 , but skip the fifth iteration 

# num = int(input("Enter the Number to get the Multiplication table of that Number: "))
# for i in range(1,11):
#     if i == 5:
#         continue
#     print(f"{num} X {i} = {num*i}")

#4. Reverse a String | Using loops 

# str = input("Write Something to see the reverse form of that: ")
# reverse_str = ""
# for char in str:
#     reverse_str = char + reverse_str
# print(reverse_str)

#5. Find the First Non-Repeated Characters  |  Given a string find the first non repeated character
# str = input("Enter the String: ")
# for char in str:
#     if str.count(char) == 1:
#         print("Character is ",char)
    
#6. Factorial Calculator |  Calculate the factorial of a number using while loops 
# number = int(input("Enter the Number to get the factorial of that Number: "))
# factorial = 1
# while number > 0:
#     factorial = factorial * number
#     number = number - 1

# print(factorial)

#7. Validate Input | Keep asking the user for input until they enter a number between 1 and 10

# while True:
#     number = int(input('Enter the  Number between 1 and 10 '))
#     if 1<= number <=10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid Number")


#8. List uniqueness checker  |  check if all elements in a list are unique . If a duplicate is found , exit the loop and print the Duplicate 

# items = ["apple","banana","orange","apple","orange","mango"]
# unique_item = set()
# for item in items:
#     if item in unique_item:
#         print("Duplicate")
#         break
#     else:
#         unique_item.add(item)


#9. Exponential Backoff |  Implement an exponential backoff strategy that doubles the wait time between retries , starting from 1 second , but stop after 5 retries .

# import time

# wait_time = 1
# max_retries = 5
# attempts = 0

# while wait_time < max_retries:
#     print("Attemps", attempts + 1, "Wait Time",wait_time)
#     time.sleep(wait_time)
#     wait_time *= 2
#     attempts += 1




#                                           Questions on Functions 

#1. Write a function to calculate and return the square of a number .  | Basic Function Syntax
# def sqr(num):
#     print(num*num)
# num = int(input("Enter the Number"))
# sqr(num)

#2. create a function that take two numbers as parameters and return their sum    |  function with multiple parameters 

def add(num1,num2):
    return num1 + num2
num1 = int(input("Enter the First Number "))
num2 = int(input("Enter the Second Number "))
result = add(num1,num2)
print(result)