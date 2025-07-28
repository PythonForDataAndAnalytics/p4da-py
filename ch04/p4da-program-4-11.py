# Using for repetition, generate a table of weights and calculated BMIS

# height is an input common to all calculations, so get outside the loop
height = float(input('Enter height (inches): '))

# These variables control the beginning, steps, and end of the table
weightMin = int(input('Minimum weight: '))
weightMax = int(input('Maximum weight: '))
weightIncr = int(input('Increment weight: '))

print() # print a blank line
print('Weight', 'BMI') # heading for table

# use for statement to generate a table, using 3-part range()
for weight in range(weightMin, weightMax+1, weightIncr):
   bmi = weight / height**2 * 703
   print(weight, ' ', round(bmi, 1))
