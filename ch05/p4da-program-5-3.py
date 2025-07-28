# two inputs, one output

# define the function
def calcTotal(numberItems, unitCost):
    totalCost =  numberItems * unitCost
    return totalCost

# get inputs
count = int(input('Enter # of books: '))
cost = float(input('Enter cost per book ($): '))

# processing - call the function
total = calcTotal(count, cost)

# display the result
print('Total: $', total)
