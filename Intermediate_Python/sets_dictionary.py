'''
Set
Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.
Sets are written with curly brackets.
'''

# sets = {"hey","How","are","you"}
# print(sets)


'''
Dictionary
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:
'''

details = {
    "fname" : "Vishal",
    "lname" : "Tiwari",
    "age" : 21,
    "location" : "Georgia"
}

print(details)
print(len(details))                 # This will give the length of a dictionary   |    We can add any data type item in dictionary
print(type(details))                # to see the data type 


#                                    Accessing the Items | We can access the dictionary with key and values 

x = details.keys()
y = details.values()
print(x)
print(y)


details.update({"fname" : "Sahil"})                    # changing or updating the dictionary 
print(details) 


# Note : Remaining all the things are same as list functions 