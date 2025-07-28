# Using while repetition and control variable,
# generate a table of weights and BMIs
# Check that weight is > 0

height = float(input('Enter height (inches): '))
keepGoing = 'y' # this is the control variable, for looping

while keepGoing == 'y':

   weight = float(input('\nEnter weight (pounds): '))

   if weight > 0:
      bmi = weight / height**2 * 703
      print('BMI = ', round(bmi, 1))
   else:
      print('Error, weight must be positive')

   keepGoing = input('Enter another weight (y/n)? ')
