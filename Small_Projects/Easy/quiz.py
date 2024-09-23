print("Welcome to the quiz Game ")

playing = input('Do you want to play: ')
if playing.lower() != "yes":
    quit()

print("Ok Let's Play This Quiz")
score = 0

answer = input("What does Central Processing unit Means: ")
if answer.lower() == "brain of the computer":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the Full form of CPU")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Who is the brain of the computer ")
if answer.lower() == "CPU":
    print("Correct")
    score += 1
else:
    print('Incorrect')

answer = input('Which alphabet is used to copy the text ')
if answer.lower() == "c":
    print('Correct')
    score += 1
else:
    print("Incorrect")

print(f"Your Total Score is {score} ")
print(f"You got {(score/4)*100} %")