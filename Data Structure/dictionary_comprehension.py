# Simple lopping
values = {}
for x in range(5):
    print(x*2)

# comprehesion
# [expression for item in items]
# expression = x*2
# item = x
# items = range
# for list comprehension
values = [x * 2 for x in range(5)]
print(values)

# for dictionary comprehension
values = {x: x*2 for x in range(5)}
print(values)

# For set comprehension
values = {x*2 for x in range(4)}
print(values)
