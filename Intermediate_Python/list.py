'''
List : Lists are used to store multiple items in a single variable.     
Lists are created using square brackets:
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
'''


# list = ["chai","cofee","blacktea","greentea"]
# print(list)                                               # This is  the basic list 
# print(len(list))                    # This is the length function we use this to know the length of a list 

# list2 = [1,2,3,4,5]
# list3 = [True,False,True]             # List item can any data types 
# list4 = ["Vishal",11,True]
# print(list4)
# print(type(list2))                     # type() function in list is used to know the data type of a list 


#                               Accessing the List Items 
#  List items are indexed and you can access them by referring to the index number:
# print(list[2])
# print(list[0:])
# print(list[1:3])
# print(list[-1])
# print(list[-4:-1])

# if "chai" in list:
#     print("Yes it is in the list")              # Checking if item is in the list 


# list[1] = "Newchai"                        # changing the list items 
# list[1:4] = ["no","no","no"]               # changing the list item from a certain range  
# list.insert(2,"Vishal")                    # changing the list using insert function 
# list.append("Newbanda")                    # Adding the new item
# list.insert(2,"chalna")                    # This is also a way to add new item
# list.extend(list3)                        # extend is used to the other list items
# list.remove("Newbanda")                    # Removing the list item 
# list.pop(2)                                # This is also used to remove the list items 
# print(list)


#                                               Loops in list
# for x in list:
#     print(x)
# thislist = ["hey","hello","How","are","you"]
# for i in range(len(thislist)):
#     print(thislist[i])


# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i = i+1



#                                           List Sorting 
# num = [12,45,75,11,3,56,6,8,89,91]
# num.sort()                                    # sorting the list in ascending order
# print(num)

# num.sort(reverse = True)                      # Sorting the list in descending order
# print(num)

# new = num.copy()                              # copying the list items 
# print(new)



# l1 = [1,2,3]
# l2 = [4,5,6]
# l1.extend(l2)                              # joining the list or adding both are same 
# l3 = l1+l2                                 # adding the lists

# print(l3)
