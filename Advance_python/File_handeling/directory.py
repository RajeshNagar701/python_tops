"""
Python Directory and Files Management

A directory is a collection of files and subdirectories. 
A directory inside a directory is known as a subdirectory.

Python has the ( os ) module that provides us with many useful methods to work with directories

import os
"""

import os


# # 1) Get Current Directory in Python
# print(os.getcwd())  

# # 2)change directory
#os.chdir('C:/Users')
# print(os.getcwd())

# 3) List Directories and Files in Python
# print(os.getcwd())
# print(os.listdir())    # list all sub-directories


# 4) Making a New Directory in Python mkdir()
# os.mkdir('test')
# print(os.listdir());

# 5) Renaming a Directory or a File
# os.rename('new_one','test_rename')


# 6) Removing Directory or File in Python  remove(),rmdir()
# os.remove("Advance_python\File_handeling\hello.txt")
# os.rmdir("test_rename")         # delete the empty directory "mydir"



"""
In order to remove a non-empty directory, we can use the 
rmtree() method inside the shutil module. For example,

"""
import shutil
shutil.rmtree("Advance_python\File_handeling\demo")  # Delete demo folder and all files inside it