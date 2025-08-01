# with for, read a file and echo its lines to the screen

# use the open() function to locate the file and connect it to the variable f
f = open('measures.txt', 'r')

# for each line in the file
for line in f:
    # remove the trailing newline that Python returns
    line = line.rstrip('\n')

    print(line)

# close the file
f.close()
