# Using while repetition and a control variable,
# calculate BMIs for a height and different weights

height = float(input('Enter height (inches): '))
anotherWeight = 'y' # this is the control variable, for looping

while anotherWeight == 'y':

   weight = float(input('\nEnter weight (pounds): '))

   bmi = weight / height**2 * 703
   print('BMI = ', round(bmi, 1))
    
   anotherWeight = input('Enter another weight (y/n)? ')
