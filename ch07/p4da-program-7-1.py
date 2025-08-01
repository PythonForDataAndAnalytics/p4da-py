# read one line from a file and display it to the screen

# use the open() function to locate the file and connect it to variable f
f = open('measures.txt', 'r')

# read the first line of the file into the string variable called aline
aline = f.readline()

# remove the trailing newline that Python returns
aline = aline.rstrip('\n')

print(aline)

# close the file
f.close()
