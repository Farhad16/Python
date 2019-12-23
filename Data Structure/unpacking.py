# list unpacking

values = list(range(5))
print(*values)  # unpacking the list
values = [*range(5)]  # unpacking the range
print(values)

# unpacking two list
list1 = [*range(3)]
list2 = [*range(4)]

new = list1 + list2
print(*new)

# dictionary unpacking
first = {"x": 1, "y": 2}
second = {"z": 3}
combined = {**first, **second}
print(combined)
