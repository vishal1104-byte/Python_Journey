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

sub1 = int(input("Enter Your marks: "))
sub2 = int(input("Enter your marks: "))
sub3 = int(input("Enter your marks: "))

avg = sum(sub1,sub2,sub3)/300 * 100

if sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print("Pass")
elif avg >= 40:
    print("pass")
else:
    print("Fail")