# Calculate the EOQ – version 2: minimum order size

# Prompt for and get inputs
demand = float(input("Enter the projected demand (units/year): "))
reorderCost = float(input("Enter the reorder cost ($/order: "))
holdingCost = float(input("Enter the holding cost ($/year/unit: "))
minOrder = float(input("Enter the minimum order size (units/order): "))

# Calculate result
eoq = (2 * demand * reorderCost / holdingCost) ** .5
orderSize = max(eoq, minOrder) # account for the minimum order size

# Display results
print("\nEconomic Order Quantity:", round(eoq))
print("Order Quantity:", orderSize)
