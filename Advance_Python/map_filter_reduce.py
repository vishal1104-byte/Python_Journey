# Map , Filter and reduce all are higher order function --> When function take function as an argument so we tell them Higher order Function 

#                                                   MAP

# def cube(x):
#     return x*x*x
# l = [1,2,3,4,5,6,7]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))                          # This is the normal way to do this 
# newl = list(map(cube,l))                             # See with the help of map it is very easy to use the function in easy way 

# print(newl)



#                                  filter() -> filter is used to access or filter the list item according to our priority

# def filter_func(a):
#     return a >= 4

# newnewl = list(filter(filter_func,l))              # This is used to access the item acording to us like I want to access list item greater than 4 . 
# print(newnewl)

# n = list(filter(lambda z: z>=4,l))
# print(n)                                        # This is filter with lambda function 


# new = list(map(lambda x: x*x*x,l))
# print(new)                                 # See This is why we use lambda and this map and all special function see how it ease our work in just 3 line code 



#                             reduce()  --> Before using reduce function we have to import the reduce Function
# The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next elements , and so on .

from functools import reduce
l = [1,2,3,4,5,6,7,8,9]
red = reduce(lambda a,b: a+b,l)                   # This is the use of reduce function 
print(red)                  