# Using while repetition, generate scenarios for weights and BMIs
# includes use of continue statement for invalid weight

# get input height 
height = float(input('Enter height (inches): '))

# repeat calculating as long as entered weight is non-zero
weight = -1 # initialize weight so at least 1 repetition executes
while weight != 0:

    weight = float(input('Enter weight (pounds), or 0 to end: '))

    if weight < 0:
        print('Error, weight must be positive')
        continue
    
    elif weight > 0:
       bmi = weight / height**2 * 703
       print('BMI = ', round(bmi, 1))
