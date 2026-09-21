"""
File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

File Handling
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

1) Raed & open

f = open("demofile.txt")
print(f.read())       # all context read
print(f.readline())   # first line
print(f.read(5))      # read 5 lines
print(f.readlines())      # read all the  lines store into the list 

# 2) create & w write & a apend =>  write

"x" - Create - will create a file, returns an error if the file exists
"a" - Append - will create a file if the specified file does not exists
"w" - Write - will create a file if the specified file does not exists

f = open("myfile.txt", "x")  # create file


with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

# 3) Delete a File

import os
os.remove("demofile.txt")

if os.path.exists("demofile.txt"):  #Check if file exists, then delete it:
  os.remove("demofile.txt")
else:
  print("The file does not exist")


"""
# create file 

# f = open("Advance_python\File_handeling\demo.txt",'w')
# print(f.read())


# f = open("Advance_python\File_handeling\demo.txt")
# print(f.read())

# #Using the with statement
# with open("Advance_python\File_handeling\demo.txt") as f:
#   print(f.read())



import os

os.remove("demofile.txt")  # Remove the file "demofile.txt":
os.rmdir("myfolder")       # To delete an entire folder, use the os.rmdir() method:

