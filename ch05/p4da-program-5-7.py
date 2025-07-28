# 2 functions (including a display function)

# calculate the pre-tax cost and tax
def calcTotal(numberItems, unitCost, taxRate):
   pretaxCost = round(numberItems * unitCost, 2)
   salesTax = round(pretaxCost * taxRate, 2)
   return pretaxCost, salesTax

# display the results
def displaySales(pretax, tax):
   print('Pre-tax: $', pretax)
   print('Tax:     $', tax)
   print('Total:   $',  pretax+tax)
   return

# inputs
count = int(input('Enter # of books: '))
cost = float(input('Enter cost per book ($): '))

# processing
pretax, tax = calcTotal(count, cost, .075)

# output
displaySales(pretax, tax)
