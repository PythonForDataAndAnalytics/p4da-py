# use if within a function

# define the function
def calcTotal(numberItems, unitCost, taxRate):
   if numberItems < 10:
      discountFactor = 1.0
   else: # discount of 10% off for 10 or more items
      discountFactor = .90
   pretaxCost = round(numberItems * unitCost * discountFactor, 2)
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
