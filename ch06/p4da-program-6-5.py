# demonstrate slicing a list

# calculate the mean of a list of numbers
def calcMean(alist):
   n = len(alist)
   sum = 0
   for i in range(n):
       sum += alist[i]
   return sum / n

# calculate a list of averages for a growing window of a list
def calcGrowingAverage(alist, r=2):
   result = []
   for i in range(len(alist)):
      sublist = alist[0:i+1] # take a slice of elements from 0 to i
      print(sublist)
      mean = calcMean(sublist) # calculate the mean of the slice
      result.append(round(mean, r)) # add the slice mean to the result
   return result

measures = [10, 10.1, 9.9, 9.6, 10.1, 9.9, 9.8, 9.9, 10.3, 10]
growingAverage = calcGrowingAverage(measures)
print()
print('Growing average:', growingAverage)
