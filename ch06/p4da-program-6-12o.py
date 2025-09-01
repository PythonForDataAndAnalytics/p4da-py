# demonstrate a list of lists

# determine which indexes have values below/above a certain value
def aboveBelow(alist, splitValue):
    result = [[], []] # initialize a list of lists
    for i in range(len(alist)):
       if alist[i] <= splitValue:
           result[0].append(i)
       else:
           result[1].append(i)
    return result
    
measures = [10, 10.1, 9.9, 9.6, 10.1, 9.9, 9.8, 9.9, 10.3, 10]

result = aboveBelow(measures, 10)

print('below/at:', result[0])
print('above:   ', result[1])
