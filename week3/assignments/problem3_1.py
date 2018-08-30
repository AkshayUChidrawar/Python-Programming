def problem3_1(txtfilename):
    """ Opens file and prints its contents line by line. """
    infile = open(txtfilename)

    sum = 0

    for line in infile:
        sum = sum + len(line)
        print(line, end="") # the file has "\n" at the end of each line already

    print("\n\nThere are", sum, "letters in the file.")

    infile.close()
	
	
def printfile (fname):
    f = open(fname)
    x = f.read()
    print (x, end="")
    f.close()

def countchar (fname):
    f = open(fname)
    sum = 0
    for line in f:
        sum = sum + len(line)
    return sum
    f.close()

def problem3_1(txtfile):
    printfile(txtfile)
    print('\n')
    s = countchar(txtfile)
    print('There are',s ,'letters in the file.', end="")