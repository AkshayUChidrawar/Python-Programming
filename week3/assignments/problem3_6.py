import sys
# sys.argv is used to command line arguments. arg[0] is the first argument, ie the input file name to be run.
f1 = open(sys.argv[1], 'r')
f2 = open(sys.argv[2], 'w')
for line in f1:
    line = line.strip("\n")
    nchar = str(len(line))
    f2.write(nchar)
    f2.write("\n")
f1.close()
f2.close()