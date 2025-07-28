# 3 inputs (1 passed as constant)
def calcTotal(numberItems, unitCost, taxRate):
    pretaxCost =  numberItems * unitCost
    aftertaxCost = pretaxCost * (1 + taxRate)
    return aftertaxCost

# get inputs
count = int(input('Enter # of books: '))
cost = float(input('Enter cost per book ($): '))

# processing - call the function
total = calcTotal(count, cost, .075)

# display the result
print('Total: $', total)
