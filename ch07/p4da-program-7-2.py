# with while, read a file and echo its lines to the screen

# use the open() function to locate the file and connect it to the variable f
f = open('measures.txt', 'r')

# read the first line of the file into the string variable called line
line = f.readline()

# while there are more lines in the file
while line != '': # while there are more lines in the file
    # remove the trailing newline that Python returns
    line = line.rstrip('\n')

    print(line)

    # read the next line of the file, if any
    line = f.readline()

# close the file
f.close()
