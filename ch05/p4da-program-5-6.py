# return 2 values from a function

# define the function
def calcTotal(numberItems, unitCost, taxRate):
    pretaxCost = round(numberItems * unitCost, 2)
    salesTax = round(pretaxCost * taxRate, 2)
    return pretaxCost, salesTax # return 2 results to the caller

# inputs
count = int(input('Enter # of books: '))
cost = float(input('Enter cost per book ($): '))

# call the function, receiving two results on the left hand side
pretax, tax = calcTotal(count, cost, .075)

# output
print('Pre-tax: $', pretax)
print('Tax:     $', tax)
print('Total:   $', pretax+tax)
