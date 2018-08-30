#with keyword is equivalent to open(). Also, it does not require to include the close() command.
"""python print() function by default ends with newline. So, if we want to continue on same line, 
we use end = '' which means that end character should be a white space & not a new line. So, next 
print statement continues on same line. Also, you can use the \n character to put the contents of 
same print statement on diferent lines [ if you use a single print statement- 
print ('First line \n Second line') ]"""

"""The reader function takes each line (row) of the input csv file and, (for each row) makes individual
list of all its columns' values. Then, you just choose the column you want the variable data for."""

import csv

def problem3_7(pricefile,flowername):
    with open(pricefile) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
               print(row)
               if flowername in row[0]:
                   print(row[1])