# Using while repetition and special end value,
# generate a table of weights and BMIs

# get input height (common for all calculations)
height = float(input('Enter height (inches): '))
while height <= 0: # validate height
    print('Error, height must be > 0.')
    height = float(input('Enter height (inches): '))

# get initial weight to calculate with
weight = float(input('Enter weight (pounds): '))
    
# repeat calculating as long as entered weight is non-zero
while weight != 0:
    bmi = weight / height**2 * 703
    print('BMI = ', round(bmi, 1))
    weight = float(input('\nEnter weight goal (or 0 to end): '))
