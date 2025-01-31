# Exception handling is the process of responding to unwanted or unexpected when a computer program runs. Exception handling is used to avoid program or system crashes .

a = input("Enter the Number: ")
print(f"The Multiplication table of {a}")

try:   # The code in try block runs when there is no error
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:      # If the try block catches the error , then the except block is executed 
    print("Some Error occured ",e)

print("Some imp lines of code ")
