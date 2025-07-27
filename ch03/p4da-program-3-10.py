# Calculate the ending balance of a 1-year certificate of deposit
# Consider new vs existing customers, and 2 rates for existing customers

# Prompt for type of customer
customer = input('Enter n if customer is new, or e for existing: ')

# Prompt for the initial investment
invest = float(input('Please enter investment amount: '))

if customer == 'e' and invest >= 1000:
   interestRate = 3.25
elif customer == 'e' and invest < 1000:
   interestRate = 3.0
else:
   interestRate = 3.5

# Calculate the ending balance
endBalance = invest * (1 + interestRate/100)

# Display the result
print('Interest rate=', interestRate, '%')
print('Ending balance= $', endBalance)
