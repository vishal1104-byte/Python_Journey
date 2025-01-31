# Handling the file when writing the file 

file = open('test.txt','w')

try:
    file.write("Hey this is something New approach from my side ")
finally:
    file.close()