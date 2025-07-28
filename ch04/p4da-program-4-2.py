# Cumulate a set of user-entered numbers

# Initialize values before repetition
count = 0 # number of values entered by user
total = 0 # keep track of the running total of user-entered values

# repetition to prompt for and cumulate total
value = float(input('Enter a value: ')) # prompt for the first value
while value != 0:
    total = total + value # keep a running total
    count = count + 1 # keep track of number of values entered
    value = float(input('Enter a value (or 0 to end): ')) # prompt for values

# Output results
print()
print('Number of values:', count)
print('Total of values:', total)
