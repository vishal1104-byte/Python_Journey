'''
File Handling
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''

# f = open('Python_Journey-1/Intermediate_Python/new.txt','r') # This is file opening
# text = f.read(10)                                                                     # This is readiing the file 
# print(text)
# print()
# print(f.read(2))                               # Read only parts of the file

# print(f.readline())                            # read lines one by one
# print(f.readline())


# for x in f:                                 # Looping the text file content 
#     print(x)

# print(f.close())                       # For closing the FIle 



#                                         Python File Writing 
'''
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
'''

# f = open("/workspaces/Python_Journey/Intermediate_Python/new.txt","a")         # This a is for appending on the previous file
# f.write("Hey This is New Line that I add")       # This is used to something new in the file
# f.close()
# f = open("/workspaces/Python_Journey/Intermediate_Python/new.txt","r")
# print(f.read())                              # After writing the new text in the file we must have to used read to open and the read the file 


# f = open("/workspaces/Python_Journey/Intermediate_Python/test.txt","x")       # This x is used to create the new file
# f = open("/workspaces/Python_Journey/Intermediate_Python/test.txt","w")
# f.write("Lets add something in the test file ")
# f = open("/workspaces/Python_Journey/Intermediate_Python/test.txt","r")
# print(f.read())  


# import os 
# os.remove("/workspaces/Python_Journey/Intermediate_Python/test.txt")             # To delete the File from the folder

# And instead of os.remove we can use rmdir to remove the folder not only file 

# with open("/workspaces/Python_Journey/Intermediate_Python/new.txt","r") as f:

#     print(f.read())             # This is also the way to open the file with "with Function "



#                               Seek() and tell() and Other Function 

# In python the seek() and tell() function are used to work with file objects and their positions within a file. 
   
# with open("/workspaces/Python_Journey/Intermediate_Python/new.txt","r") as f:
#     f.seek(10)                         # Seek function read the file from the no of bits that was set like 10 so it read the file from the 10th character
#     f.truncate(10)                   # This function is used to set the file only with 10 characters or byte    
#     print(f.read())
#     print(f.tell())                 # tell() function tells us the exact position where we are  

    



# f = open('Python_Journey-1/Intermediate_Python/new.txt','a')
# f.write("Hey This Denial also know as Vishal")
# f.close()
# f = open('Python_Journey-1/Intermediate_Python/new.txt','r')
# text = f.read()
# print(text)


# f = open('Python_Journey-1/Intermediate_Python/test.txt','x')
# f = open('Python_Journey-1/Intermediate_Python/test.txt','w')
# f.write("Hey we are adding something in file to check what we learn in the file objects ")

# f = open('Python_Journey-1/Intermediate_Python/test.txt','r')
# text = f.read()
# print(text)



# f = open('Python_Journey-1/Intermediate_Python/test.txt','r')
# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]

#     print(f"Mark of student {i} in maths is {m1}")
#     print(f"Mark of student {i} in Science is {m2}")
#     print(f"Mark of Student {i} in English is {m3}")
#     print(line)


f = open('Python_Journey-1/Intermediate_Python/test.txt','r')
f.seek(10)                 # Seek bolta hai jo number diya hai na wohi se start karne ka jaise 10 no. se start karna hai yaha pe aur uske aage se hi read karega 
data = f.read()
print(data)
