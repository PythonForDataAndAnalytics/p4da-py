# Calculate BMI, given height and weight

# Prompt for inputs
height = float(input("Enter height (inches): "))
weight = float(input("Enter weight (pounds): "))

# Calculate the BMI result:
bmi = weight / (height ** 2) * 703

# Display the result
print("BMI =", bmi)
