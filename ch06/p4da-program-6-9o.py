# Compare means of two lists, and their combinations using extend()

# calculate the mean of a numeric list, rounded to r decimal places
def calcMean(alist, r=2):
   n = len(alist)
   if n == 0:
       return None # handle an empty list
   sum = 0
   for i in range(n):
       sum += alist[i]
   return round(sum / n, r)

# 2 lists of measures
measures1 = [10, 10.1, 9.9, 9.6, 10.1, 9.9, 9.8, 9.9, 10.3, 10]
measures2 = [9.9, 10.0, 9.9, 9.6, 10.1, 9.5, 9.7, 9.8, 10.1, 9.9]

# calculate means of each list
mean1 = calcMean(measures1)
mean2 = calcMean(measures2)

# Use extend to consolidate the list and determine an overall mean
measures1.extend(measures2)
meanAll = calcMean(measures1)

print(mean1, mean2, meanAll)
