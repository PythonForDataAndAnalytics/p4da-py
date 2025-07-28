# Using while repetition and special end value, generate BMI scenarios
# includes use of break statement to end looping

# get input height (common for all calculations)
height = float(input('Enter height (inches): '))

# get initial weight to calculate with
weight = float(input('Enter weight (pounds): '))

# repeat calculating as long as entered weight is non-zero
while True:
    if weight == 0:
        break
    
    bmi = weight / height**2 * 703
    print('BMI = ', round(bmi, 1))
    
    weight = float(input('\nEnter weight goal (or 0 to end): '))

print('Program ends')
