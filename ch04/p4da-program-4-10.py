# Using for repetition, prompt for weights and calculate several BMIs

# height is an input common to all calculations, so outside the loop
height = float(input('Enter height (inches): '))

# n will be the number of times the loop executes
n = int(input('Number of BMIs to calculate: '))

for i in range(n): # control the number of times the loop executes

   weight = float(input('\nEnter weight (pounds): '))

   bmi = weight / height**2 * 703
   print('BMI = ', round(bmi, 1))
