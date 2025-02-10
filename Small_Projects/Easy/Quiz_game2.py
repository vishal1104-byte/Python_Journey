#                                                  An Advance Quiz game 

questions = (
    "What is the capital of India",
    "Who is the first prime minister of India",
    "What is the national animal of India ",
    "Who is modiji",
    "Who is Vishal",

)

options = (("A. Delhi ","B. Mumbai ","C. Uttar Pradesh ","D. Punjab "),
          ("A.Jawaharla Nehru ","B. Lala lajpat rai","C. Rajendra Prasad ","D. Mahatma Gandhi "),
          ("A. Lion ","B. Tiger ","C. Peacock","D. Elephant"),
          ("A. Prime Mininster","B. Home Minister","C. Chief Minister","D. Judge"),
          ("A. Sahil","B. Yash ","C. Shivam","D. Piyush"))

answers = ("A","A","B","A","A")

guesses = []

scores = 0

question_num = 0


for question in questions:
    print("----------------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Choose Your Answer (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        scores += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The Correctec answer is {answers[question_num]}")
    question_num += 1

print("------------------------------------------------")
print("                      Result                    ")
print("------------------------------------------------")

print("answers: ",end = "")
for answer in answers:
    print(answer,end=" ")
print()

print("Guesses: ",end = "")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(scores / len(questions) * 100)
print(f"Your Score is {score}%")