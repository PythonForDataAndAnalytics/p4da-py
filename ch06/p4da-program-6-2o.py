# show how to create an empty list and add elements to it

# prompt for a series of values and build and return a list
def getValues():
    result = [] # define an empty list
    entry = input('Enter a value, or <return> when done: ')
    while entry != '':
        result.append(float(entry)) # add a value to end of list
        entry = input('Enter a value, or <return> when done: ')
    return result

# calculate the mean of a list
def calcMean(alist):
   n = len(alist) # determine the number of elements in the list
   if n == 0:
       return None # handle an empty list
   sum = 0 # sum will cumulate the list's values
   for i in range(n):
       sum += alist[i]
   return sum / n # calculate and return the average

measures = getValues()
mean = calcMean(measures)
print('Mean=', mean)
