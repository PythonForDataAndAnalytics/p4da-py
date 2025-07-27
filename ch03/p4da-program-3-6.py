# Calculate the ending balance of a 1-year certificate of deposit (2 rates)

# Prompt for the initial investment
invest = float(input('Please enter investment amount: '))

# Determine the interest rate, depending on the size of the investment
if invest >= 1000:
   interestRate = 3.25
else:
   interestRate = 3.0

# calculate the ending balance
endBalance = invest * (1 + interestRate/100)

# display the result
print('Interest rate=', interestRate, '%')
print('Ending balance= $', endBalance)
