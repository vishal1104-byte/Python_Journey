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

'''
A String in python can be sliced for getting a part of the string .
The index in a string starts from 0 to (length -1) in python. In order to slice a string we use the following syntax 
'''

'''
str = "Jaldi Jaldi koi achi ladki meri Girlfriend ban jaaye "
print(str[2])           # It will provide l as an output as "l" position at 2
print(str[0:6])         # It will provide "jaldi" as an ouput 
print(str[0:])          # It will provide full string as an ouput 
print(str[:-1])         # It will provide full string as an output 
print(str[1:8:2])       # It is the slicing with skip value 
'''

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
