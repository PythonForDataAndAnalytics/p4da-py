# This program demonstrates an infinite loop error

#initialization
i = 1 # starting value for the table
n = 5 # ending value for the table

# using repetition, generate the table
while i <= n: # condition will always be true
    # calculation and display
    print(i, i**2, i**3)
    
    # missing statement below here should increment variable i
    # instead, i is stuck at 1
