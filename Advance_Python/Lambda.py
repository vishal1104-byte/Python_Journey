'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
'''

def double(x):
    return x*5

print(double(5))                               # Basically we used this method to make the function 

# Now in Lamda we use function as a anonymous without creating the function 

Double = lambda x : x*2                  # See we did same thing on both the function but here we make function without creating it anonymously
print(Double(5))
square = lambda a : a*a
print(square(5))
cube = lambda b : b*b*b
print(cube(3))

add = lambda c,d : c + d
print(add(6,9))

multiply = lambda a,b,c: a*b*c
print(multiply(1,2,3))


# The Lambda main uses is that it can used in the another function very easily 

def my_func(n):
    return lambda a: a*n
mytripler = my_func(3)
print(mytripler(11))


def appl(fx,value):
    return 6 + fx(value)

print(appl(cube,2))