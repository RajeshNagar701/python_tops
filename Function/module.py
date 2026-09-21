"""
Python Modules
As our program grows bigger, it may contain many lines of code. 
Instead of putting everything in a single file, we can use modules to separate codes 
in separate files as per their functionality. This makes our code organized and easier to maintain.

Module is a file that contains code to perform a specific task. 
A module may contain variables, functions, classes etc. Let's see an example,


1) example.py

def add(a, b):   # Python Module addition
   result = a + b
   return result

2) Import modules in Python
We can import the definitions inside a module to another module or the interactive 
interpreter in Python.

import example


Standard Module

Python has tons of standard modules. You can check out the full list of 
Python standard modules and their use cases.


math              math.sqrt(25) 
random            random.randint(1, 10) 
datetime          datetime.datetime.now() 
os 


"""

import sum
print(sum.add(5,5))  # returns 10




# # Import Python Standard Library Modules
# # import standard math module 

# import math
# print("The value of pi is", math.pi) # use math.pi to get value of pi


# #Python import with Renaming
# import math as m  # import module by renaming it

# print(m.pi)   # Output: 3.141592653589793


# # import only pi from math module
# from math import pi
# print(pi)     # Output: 3.141592653589793


# # import all names from the standard module math
# from math import *
# print("The value of pi is", pi)



# The dir() built-in function : In Python, we can use the dir() function to 
# list all the function names in a module.

print(dir(sum))
