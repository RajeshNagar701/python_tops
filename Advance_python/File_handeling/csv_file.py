"""
The CSV (Comma Separated Values) format is a common and straightforward way to 
store tabular data. To represent a CSV file, it should have the .csv file extension.

Now, let's proceed with an example of the info .csv file and its data.

want to get datafrom csv file then have to import csv

import csv

csv.reader()           # Read CSV Files with Python in list 
csv.DictReader(file)   # print each row as a dictionary.

csv.writer(file )      # write to a CSV file 
csv.writer(file, delimiter='|') # write to a CSV file with | delemeter
csv.DictWriter()       # class to write dictionary data into a CSV file
"""

# Read CSV Files with Python
# The csv module provides the csv.reader() function to read a CSV file.

import csv

# with open('Advance_python\File_handeling\mydata.csv', 'r') as file:
#     reader = csv.reader(file)   
#     for row in reader:
#         print(row)

#===============================================================================

# with open('Advance_python\File_handeling\mydata1.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "Movie", "Protagonist"])
#     writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
#     writer.writerow([2, "Harry Potter", "Harry Potter"])


# Writing Multiple Rows with writerows()

# row_list = [["SN", "Name", "Contribution"],
#              [1, "Linus Torvalds", "Linux Kernel"],
#              [2, "Tim Berners-Lee", "World Wide Web"],
#              [3, "Guido van Rossum", "Python Programming"]]
# with open('protagonist.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(row_list)


#===============================================================================


# with open('Advance_python\File_handeling\mydata2.csv', 'w', newline='') as file:
#     fieldnames = ['player_name', 'fide_rating']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
#     writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
#     writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})


#===============================================================================

"""
Pandas : install and import it

Using Python Pandas to Handle CSV Files

Pandas is a popular data science library in Python for data manipulation and analysis.
If we are working with huge chunks of data, it's better to use pandas to handle CSV files for 
ease and efficiency.

"""