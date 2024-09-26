# Conditional statement is used for making decisions if this so print this else print something else 

'''
Syntax : 
if(condtion):
    print("yes")
elif(condition):
    print("No")
else:
    print("maybe")
'''


'''
Relational Operator -->   relational opeartor are used to evaluate the condition inside the if statements
==  --> Equals 
>=  --> Greater than equals
<=  --> Less than equals,etc

Logical Operators  -->    Loogical operator opearte on conditional statements 
and -->  true if both operands are true else false 
or --> true if atleast one opearand is true else false 
not --> inverts true to false & false to true 
'''


'''
Important Notes : 
1. There can be any numbers of elif statements 
2. Last else is executed only if all the conditions inside elif fails 
'''




 #  Example -->  whether you are eligible to vote or not 
a=int(input("Enter your age "))
if(a>=18):
  print("You are Eligible to vote ")
elif(a<=18):
  print("You are not Eligible to vote ")
else:
  print("You can vote ")



appleprice=int(input("Enter the price of apple "))
budget=int(input("Enter your Budget "))
if(appleprice>budget):
    print("oops sorry you can afford it  ")
elif(appleprice==budget):
    print("you can buy shall we proceed further")
else:
    print("we will go for it then ")