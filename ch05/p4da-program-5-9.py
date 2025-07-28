# 3 functions plus main() (function calling other functions)

# prompt user for inputs
def getSalesInfo():
    count = int(input('Enter # of books: '))
    cost = float(input('Enter cost per book ($): '))
    return count, cost

# calculate the pre-tax cost and tax
def calcTotal(numberItems, unitCost, taxRate):
    pretaxCost = round(numberItems * unitCost, 2)
    salesTax = round(pretaxCost * taxRate, 2)
    return pretaxCost, salesTax

def displaySales(pretax, tax):
   print('Pre-tax: $', pretax)
   print('Tax:     $', tax)
   print('Total:   $', pretax+tax)

# call each function for input, processing, and output
def main():
   count, cost = getSalesInfo()
   pretax, tax = calcTotal(count, cost, .075)
   displaySales(pretax, tax)

main()
