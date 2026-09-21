"""
Package

Suppose you have a large application:

A package is a container that contains various functions to perform specific tasks. 
For example, the math package includes the sqrt() function to perform the square root of a number.

While working on big projects, we have to deal with a large amount of code, 
and writing everything together in the same file will make our code look messy. 
Instead, we can separate our code into multiple files by keeping the related code together in packages.

Now, we can use the package whenever we need it in our projects. 
This way we can also reuse our code.


Eample : 

Game Package------>  __init__.py
                --->  Sound  
                       __init__.py
                       load.py
                       play.py
                       pause.py
                ---> Image
                     __init__.py
                       open.py
                       change.py
                       close.py    


1) Importing module from a package

import Game.Sound.play   ##we want to import the start module in the above example 

Game.Sound.play.select_diff(2)  # module contains a function named select_diff(), we must use the full name to reference it.


2) Import Without Package Prefix

from Game.Sound import play

play.select_diff(2)  # We can now call the function simply as follows:


3) Import Required Functionality Only

from Game.Sound.play import select_diff
select_difficulty(2)  # Now we can directly call this function.


What is __init__.py?

Traditionally, __init__.py is used to mark a directory as a Python package
and can contain package initialization code.

 
Standard Library Packages
 
import os 
import json 
import datetime 
import math 
import random 

Third-Party Packages 

A popular tool for installing them is pip. 

pip install requests 


What is pip?
pip is the standard package-management tool commonly used with Python.
It can install Python packages from the Python Package Index (PyPI).
pip --version 
      

Package vs Module

       Module	                                                 Package
A single .py file	                                   A folder/directory containing modules
Contains functions, classes, variables	              Organizes related modules
Example: calculator.py	                            Example: calculator/
import calculator	                                   from calculator.addition import add

"""


