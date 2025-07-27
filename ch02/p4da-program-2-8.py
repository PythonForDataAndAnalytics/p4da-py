# Calculate the economic order quantity (EOQ)

# Prompt for and get inputs
demand = float(input("Enter the projected demand (units/year): "))
reorderCost = float(input("Enter the reorder cost ($/order): "))
holdingCost = float(input("Enter the holding cost ($/year/unit): "))

# Calculate result
eoq = (2 * demand * reorderCost / holdingCost) ** .5

# Display result
print("Economic Order Quantity:", round(eoq))
