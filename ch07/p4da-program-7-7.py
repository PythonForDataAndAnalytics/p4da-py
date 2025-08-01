# Prompt for input and write a single line to a file

name = input('Enter your name: ')

# open a file called greeting.txt for writing, and associate variable fout
fout = open('greeting.txt', 'w')

# use print() function to write a line to the file
print('Hello,', name, file=fout)

# close the file
fout.close()
