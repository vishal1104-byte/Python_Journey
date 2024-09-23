name = input('Enter Your Name: ')
print(f"Welcome {name} Lets with your journey and you can choose your own adventure ")

answer = input("You are on a dirty road , it has come to an end and you can go left or right . Which way would you like to go ?").lower()

if answer == "left":
    answer = input("You come to a river , you can waly around it or you can swim ? type walk if you want to walk and type swim if you want to swim")
    if answer == "swim":
        print("You swim across the river and alligator eat you , You Lose !")
    elif answer == "walk":
        print("You walked for a miles ran out of the water and you lose !")
    else:
        print("Not a Valid option , You lose ")

elif answer == "right":
    answer = input("You came to a bridge , it looks wobbly do you want to cross it or head back ? \n Write cross if you want to cross it and write back if you want to go back  ")
    if answer == "back":
        print("You go back and you lose !")
    elif answer == "cross":
        answer = input("You cross the bridge and you see one stranger Do you want to meet that stranger or no? \n  write yes if you want to meet and type no if you dont want to meet ")
        if answer == "no":
            print("You avoid to meet the stranger and you get nothing hence you lose !")
        elif answer == "yes":
            print("Congratulation You won Because you meet with stranger and he give you 1 kg Gold ")
        else:
            print("Not a valid option , you lose!")
    else:
        print("Not a valid option you lose!")

else:
    print("Not a valid Option you Lose!")


print("Thank You for trying ", name)