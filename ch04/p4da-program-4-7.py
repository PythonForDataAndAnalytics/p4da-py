# Using while repetition, generate a table of
# CD interest rates and interest earned

invest = float(input('Enter initial investment ($): '))
years = int(input('Enter years: '))

rateMin  = float(input('Minimum rate: '))
rateMax  = float(input('Maximum rate: '))
rateIncr = float(input('Increment rate: '))

# print the header rows for the table
print()
print('Interest', 'Interest')
print('    Rate', '  Earned')

# generate a table of interest rates and corresponding interest earned
rate = rateMin # the initial rate for the table
while rate <= rateMax:
   endBalance = invest * (1 + rate/100) ** years
   interest = endBalance - invest
   
   print(format(rate,'8.3f'), format(interest, '8,.2f'))
   
   rate += rateIncr # the next rate
