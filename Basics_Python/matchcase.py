# Match Case :
# Like Switch case use in c , java and all in python we use match case      ||   A match statement will compare a given variable's value to different shapes , also reffered to as the pattern 

# x = int(input("Enter the Number: "))
# match x:
#     case 0:
#         print("X is zero")
#     case 4:
#         print("X is Four")
#     case _: 
#         print(x)                            # This is just the Normal Exercise for example 



# Example of normal calculator using match case 

num1 = int(input("Enter the FIrst Number: "))
num2 = int(input('Enter the Second Number: '))
x = input("Enter the Mathematical Operator you have to perform ( + , - , * , /)")

match x:
    case '+':
        print(num1 +num2)
    case '-':
        print(num1 - num2)
    case '*':
        print(num1 * num2)
    case '/':
        print(num1 / num2)