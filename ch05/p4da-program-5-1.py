# define and use a function to display a greeting

# the hello() function has 1 parameter: 'nameParameter'
def hello(nameParameter):
    print('Hello,', nameParameter, '!')

name = input('Please enter your name: ')
hello(name) # call the function with the argument 'name'
