# demonstrate the use of del to remove elements from a list

# based on a provided list, create a new list
# that excludes values outside of a certain range
def trimOutliers(alist, lo, up):
    list2 = alist.copy() # make a distinct copy of the list argument
    for i in range(len(alist)-1, -1, -1): # work backwards through the list
       # if the list element value is outside the range, remove it
       if (alist[i] < lo) or (alist[i] > up):
           del list2[i] # del removes this item from the list
    return list2

# an original list
measures = [10, 10.1, 9.9, 9.6, 10.1, 9.9, 9.8, 9.9, 10.3, 10]

# create a new list with values remove that are outside of [9.9, 10.1]
measures2 = trimOutliers(measures, 9.9, 10.1)

# display original and trimmed list
print(measures)
print(measures2)
