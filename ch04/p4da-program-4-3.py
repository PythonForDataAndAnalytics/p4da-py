# Find the maximum of a set of user-entered numbers

# repetition to prompt for values and track largest
value = float(input('Enter an initial value: ')) # prompt for the first value
largest = value
while value != 0:
    if value > largest: # is latest entry larger than the largest so far?
        largest = value # if so, track this as the new largest value
        print('New largest value:', largest)
    # prompt for subsequent values
    value = float(input('Enter another value (or 0 to end): ')) # 

# Output result
print('\nLargest value:', largest)
