# with for, read a file of numbers
# and calculate and display their average

total = 0 # the total of all values read
i = 0 # the number of values read

f = open('measures.txt')
for line in f:
    line = line.rstrip('\n').strip()
    if line != '': # ignore blank lines
       value = float(line) # the variable line is of type str, convert to number
       print('value ', i+1, ': ', line, sep='')
       total += value
       i += 1

f.close()
average = total / i
print("average =", round(average, 2))
