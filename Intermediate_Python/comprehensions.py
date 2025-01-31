
# Adding the List elements in list by using the loops 

# my_list = []
# for i in range(10):
#     while True:
#         nums = int(input(f"Enter the Number You want to add in the List {i + 1}: "))
    
#         my_list.append(nums)
#         break
# print(my_list)

# This is list comprehension 
# nums = [1,2,3,4,5,6,7,8,9]
# my_list = [n for n in nums if n%2 == 0]
# print(my_list)

# Using a map and lambda function 
# nums = [1,2,3,4,5,6,7,8,9]
# my_list = map(lambda n: n*n,nums)
# print(list(my_list))

# using a filter and lambda function 
# nums = [1,2,3,4,5,6,7,8,9]
# my_list = filter(lambda n: n*n,nums)
# print(list(my_list))


# I want a (letter,num) pair for each letter in 'abcd' and each number in '0123'
# num = [1,2,3,4,5,6,7,8,9]

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num))
# print(my_list)

# Boys_names = input("Enter the Name of Boys: ")
# Girls_names = input("Enter the Names of Girls: ")
# Jodi = {
#     "Vishal":"Khushbu",
#     "Piyush":"Sanskriti",
#     "Abhay":"Kashish",
#     "Harsh":"Lakshika",
#     "Shivam":"Aditi"
# }
# Matched = []

# for boy,girl in Jodi.items():
#     if boy in Boys_names and girl in Girls_names:
#         Matched.append((boy, girl))
# print(Matched)

# if len(Matched) == len(Jodi):
#     print("Perfect Matched")
# else:
#     print("some matches are missing")




#                                         Dictionary Comprehension 
# names = ['Vishal','shivam','piyush','abhay','harsh']
# heroes = ['Batman','Superman','Spiderman','Deadpool','wolvorine']

# my_dict = {}
# for name, hero in zip(names,heroes):           # This zip function is used to merge the list and make the dictionaries
#     my_dict[name] = hero
# print(my_dict)

# my_dict = {name : hero for name,hero in zip(names,heroes) if name != 'Vishal'}
# print(my_dict)                                  # Same FUnction by using Dictionaries comprehension  


#                                             Set Comprehensions
# nums = [1,2,3,4,6,6,8,5,7,1,2,9,7,8,3,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)


# nums = [1,2,3,4,6,6,8,5,7,1,2,9,7,8,3,9]
# my_set = {n for n in nums}                           # same thing but using set comprehensions 
# print(my_set)
# print(type(my_set))