# Using while repetition and a bool control variable,
# calculate BMIs for a height and different weights

height = float(input('Enter height (inches): '))
anotherWeight = True # this is the control variable, for looping

while anotherWeight:

   weight = float(input('\nEnter weight (pounds): '))

   bmi = weight / height**2 * 703
   print('BMI = ', round(bmi, 1))
    
   reply = input('Enter another weight (y/n)? ')
   anotherWeight = (reply == 'y')
