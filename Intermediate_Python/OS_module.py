# OS Module :-  The OS Modules allows to interact with the underlying Operating System  |  It is used for handling task like file and directory operations .


import os
print(os.getcwd())                      # It will give the Current working directory 

os.chdir('/Users/Vishal/Downloads/')     # It will help to change the directory 
print(os.getcwd())                      # It will give the Current working directory after changing the directory


print(os.listdir())                # It will give us all the list of directories which is present in the directory 