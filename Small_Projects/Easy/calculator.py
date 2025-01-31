# This is a simple calculator 

operator = input("Enter Your Operator (+ - * /)")
num1 = int(input("Enter the first Number "))
num2 = int(input("Enter the Second Number "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2 
elif operator == "*":
    result = num1 * num2 
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid Operator")


print("The Result is ", result)