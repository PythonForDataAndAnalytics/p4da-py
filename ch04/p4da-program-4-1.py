# Using while repetition, generate a table of squares and cubes

#initialization
i = 1 # starting value for the table
n = 5 # ending value for the table

# using repetition, generate the table
while i <= n: # condition
    # calculation and display
    print(i, i**2, i**3)
    
    # change value before restarting loop
    i = i + 1

print('Program ends')
