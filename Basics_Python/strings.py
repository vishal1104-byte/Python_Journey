'''
String is a datatype in python 
String is a sequence of character enclosed with quotes 

We can primarily write a string in three ways 
single quotes  -->  a = 'Vishal'
Double quotes  -->  a = "Vishal"
Tripple quotes -->  a = ''''''
''' 

#                                           Position of the strings 
'''
x = "Hello , vishal how are you buddy ! "
print(len(x))                        # It will give the length of the strings 
print("how" in x)                    # It will give output as True bcz it is present in the string 
print("the" in x)                    # It will give output as False bcz it is not present in the string 
'''

#                                                 String Slicing
# String indexing - accessing the elements of a sequence using [] 
'''
A String in python can be sliced for getting a part of the string .
The index in a string starts from 0 to (length -1) in python. In order to slice a string we use the following syntax [start : end : step]
'''

'''
str = "Jaldi Jaldi koi achi ladki meri Girlfriend ban jaaye "
print(str[2])           # It will provide l as an output as "l" position at 2
print(str[0:6])         # It will provide "jaldi" as an ouput 
print(str[0:])          # It will provide full string as an ouput 
print(str[:-1])         # It will provide full string as an output 
print(str[1:8:2])       # It is the slicing with skip value 
'''

# str = "https://vishal.com"
# print(str[::-1])                             # Reverse the string

#                                                 Strings Functions

# Some of the mostly used functions to perform operations on or manipulate strings are :

# str = "Vishal is so smart"
''' 
1. len() function --> This function returns the length of ths string
2. string.endswith()  --> This function tells whether the variable strings ends with the string or not 
3. string.count()    --> This function counts the total number of occurence of any character 
4. string.capitalize()  --> This function capitalize the first character of a given string 
5. string.find(word)  --> This function finds a word and returns the index of first occurence of that word in the string 
6. string.replace(newword,oldword)  --> This function replaces the oldword with newwords in the entire string 
7. str.isdigit  -- > Give the boolean valur of True or false 
'''
# print(len(str))
# print(str.endswith("art"))
# print(str.count("i"))
# print(str.capitalize())
# print(str.find("vishal"))
# print(str.replace("Vishal","Sahil"))



#                                     Escape Sequence Character  --> Sequence of character after backslash \

'''
\n -> Newline
\t -> Tab
\ -> Single quote 
\\ -> backslash 
'''



#                                      Advance String Formating 

# person = { "name":"Vishal","age":21}

# sentence = "My name is {0} and I am {1} years Old".format(person["name"],person["age"])   # This format function is used to format the string in Dictionaries 
# print(sentence)



# Exercises 

#1. Validate user Input   |  Username not more than 12 char | username must not contain spaces | Must not contain digit 

# userName = input("Enter Your User Name: ")
# if len(userName) > 12 or userName.find(" ") or userName.isdigit:
#     print("Invalid User Name ")
# else:
#     print("Okay You are Valid You can use this User Name ")


str = "Hey this is Denial I am calling you from the national do not call list department SO what we do we try to find your place"
print(str[-4:])