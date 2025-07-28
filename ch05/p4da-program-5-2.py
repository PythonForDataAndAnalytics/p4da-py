# one input, one output (assumes all books are $17.50)

# define the function
def calcTotal(numberItems):
    totalCost = 17.50 * numberItems
    return totalCost

# input
count = int(input('Enter # of books: '))

# processing - call the function
total = calcTotal(count)

# output
print('Total: $', total)
