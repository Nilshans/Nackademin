import sys

names = ["Dan", "Eric", "Martin", "Gustaf", "Anders"]
ages = [21, 42, 34, 35, 22]
sizes = [39, 43, 41, 44, 36]
profileIndex = []

x = 1
sizes.sort()
lengthOfSizes = len(sizes)
medianIndex = (lengthOfSizes+1)/2
oldestIndex = len(ages)


print(medianIndex)
# print(names[x], ages[x], sizes[x])
