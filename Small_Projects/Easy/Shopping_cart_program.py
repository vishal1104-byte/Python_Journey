#                                  A SHOPPING CART PROGRAM

Foods = []
Prices = []
total = 0

while True:
    food = input("Enter the Food to buy ? (q to quit)")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the Price of {food} you buy"))
        Foods.append(food)
        Prices.append(price)

print("-------------------- Your Cart ------------------------")
for food in Foods:
    print(food,end=",")

for price in Prices:
    total += price

print(f"Your Total is {total} rs")