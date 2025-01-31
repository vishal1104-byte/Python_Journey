# This is the Temperature coverter which converts the celcius into Fahrenheit (C/F):

unit = input("Is this Temperature in celsius or Fahrenheit (C/F): ")
temp = int(input("Enter the Temperature: "))

if unit == "C":
    temp = (9 * temp / 5 + 32)
    print(f"The Temperature in Fahrenheit is {temp} Degree F")
elif unit == "F":
    temp = ((temp - 32) * 5 / 9)
    print(f"The Temperature in Celsius is {temp} Degree C")
else:
    print("Invalid Unit You are providing ")