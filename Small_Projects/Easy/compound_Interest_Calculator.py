                                   #  A COMPOUND INTEREST CALCULATOR 


principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the Principle Amount: "))
    if principle < 0 :
        print("The principle amount cant be a Zero or less than Zero ")
    else:
        break

while True :
    rate = float(input("Enter the Rate of Interest: "))
    if rate < 0 :
        print("The rate of interest cant be a Zero or less than Zero ")
    else:
        break

while True :
    time = int(input("Enter the Time Period: "))
    if time < 0 :
        print("The Time Period cant be a Zero or less than Zero ")
    else:
        break

final_amount = principle * pow((1 + rate / 100) , time)
print(f"Balance after {time} years is {final_amount:,.2f}")