list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# combine a list into a one list with a single tuple
x = list(zip(list1, list2))
print(x)

# zip can also add single character with the list as it takes a string which is iterable
y = list(zip("abcd", list1, list2))
print(y)
