# Here the new thing I learn from the basic is 
# what is expression 
# A exxpression is the combination of operators and values 

import random

secret_num = random.randint(1,10)

print("I want to see that You can choose the correct Number or not ")

for guess in range(1,7):
    guess = int(input('Enter Your Guess: '))
    if guess > secret_num :
        print("You are High")
    elif guess < secret_num:
        print("You are Low")
    else:
        break

if guess == secret_num:
    print("Correct Guess")
else:
    print("No not right")