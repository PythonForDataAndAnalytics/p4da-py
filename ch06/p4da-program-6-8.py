# demonstrate list indexing on the left-hand side

# determine counts of items above or below a certain value
def aboveBelow(alist, splitValue):
    result = [0, 0] # this list will track counts below/above splitValue
    for i in range(len(alist)):
       if alist[i] <= splitValue: result[0] += 1
       else: result[1] += 1
    return result
    
measures = [10, 10.1, 9.9, 9.6, 10.1, 9.9, 9.8, 9.9, 10.3, 10]

result = aboveBelow(measures, 10)

print(result)
