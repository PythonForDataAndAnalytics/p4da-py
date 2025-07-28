# named argument

# define the function, including a named argument
def calcTotal(numberItems, unitCost, taxRate, decimals=2):
    pretaxCost = round(numberItems * unitCost, decimals)
    aftertaxCost = round(pretaxCost * (1 + taxRate), 2)
    return aftertaxCost

# inputs
count = int(input('Enter # of books: '))
cost = float(input('Enter cost per book ($): '))

# processing – call the functions
total = calcTotal(count, cost, .075, decimals=0)

# output
print('Total: $', total)
