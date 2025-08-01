# demonstrate the use of for, to iterate over a list's elements

# calculate the mean of a list of numbers
def calcMean(alist):
   sum = 0
   for value in alist: # iterate over the elements of the list
       sum += value
   return sum / len(alist)

measures = [10, 10.1, 9.9, 9.6, 10.1, 9.9, 9.8, 9.9, 10.3, 10]
mean = calcMean(measures)
print('Mean=', mean)
