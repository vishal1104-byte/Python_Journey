# Modules in python are files containing python code that can be reused in other python programs 
# There are Three types of Module 
#1. Built in Modules --> os,math,random,datetime,calender,sys,etc  (it comes with python with standard functionalities)
#2. Third Party Modules --> These modules are installed from external sources , typically using pip (numpy,pandas,matplotlib,requests,etc)
# 3. Custom modules --> You can create your own module by saving python code in .py 


# import sys
# sys.path.append('C:\Users\Vishal\Downloads\learnpythonongithub\Python_Journey-1\Intermediate_Python\Importing_Modules\my_module')
# from my_module import *
# courses = ['History','Math','Physics','CompSci']

# index = find_index('courses','Math')
# print(index) 
# print(sys.path)

# import random
# courses = ['History','Math','Physics','CompSci']
# random_choices = random.choice(courses)
# print(random_choices)

import datetime
today = datetime.date.today()
print(today)

import calendar 
print(calendar.isleap(2020))

import os 
print(os.getcwd())