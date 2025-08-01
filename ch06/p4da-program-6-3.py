# demonstrate use of for and range(), to iterate over the list's elements

# calculate the mean of a list of numbers
def calcMean(alist):
   n = len(alist)
   if n == 0: return None # handle an empty list
   sum = 0
   for i in range(n):
       sum += alist[i] # access item i from the list
   return sum / n

measures = [10, 10.1, 9.9, 9.6, 10.1, 9.9, 9.8, 9.9, 10.3, 10]
mean = calcMean(measures)
print('Mean=', mean)
