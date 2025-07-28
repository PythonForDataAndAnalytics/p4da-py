# 3 functions (including an input function w/ no parameters)

# prompt user for inputs
def getSalesInfo():
    count = int(input('Enter # of books: '))
    costPerItem = float(input('Enter cost per book ($): '))
    return count, costPerItem

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

# input, processing, output
count, costPerBook = getSalesInfo()
pretax, tax = calcTotal(count, costPerBook, .075)
displaySales(pretax, tax)
