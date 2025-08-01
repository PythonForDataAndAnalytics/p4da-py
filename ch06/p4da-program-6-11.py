# demonstrate sorting of a list
measures = [10, 10.1, 9.9, 9.6, 10.1, 9.9, 9.8, 9.9, 10.3, 10]

# create a new sorted list, separate from a provide list
measuresSorted = sorted(measures)
print(measuresSorted)
print(measures)

# sort a list in place
measures.sort()
print(measures)
