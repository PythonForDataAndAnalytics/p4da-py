# Using for repetition, generate table of
# annual CD balances and interest

# get input parameters for the CD
initial = int(input('Initial investment ($): '))
years = int(input('Number of years: '))
interestRate = float(input('Interest rate (%): '))

# set up variables used in the loop
balance = initial
interestRateDecimal = interestRate / 100

print('\nyear', '   start', 'interest', '     end') # header for table

# for each year, calculate and display balances and interest earned
for year in range(1, years+1):
    interestEarned = int(balance * interestRateDecimal) # round down
    end = balance + interestEarned
    
    print(format(year,'4d'), format(balance, '8,d'),
          format(interestEarned, '8,d'), format(end, '8,d'))
    
    balance = end # roll over balance from year end to next year start
