# Calculate difference and percent difference between two values

# Prompt for and get inputs
salesHistory = float(input("Please enter last year's sales: "))
salesProjected = float(input("Please enter this year's projected sales: "))

# Calculate results
salesChange = salesProjected - salesHistory
salesChangePct = salesChange / salesHistory * 100

# Display results
print("Projected sales change:", round(salesChange, 1))
print("Projected sales % change:", round(salesChangePct,1))
