items = [
    ("Product1", 10),
    ("Product2", 25),
    ("Product3", 20)
]

x = list(map(lambda item: item[1], items))
# list comprehension [expression for item in items]

result = [item[1] for item in items]
print(result)

# it gives a boolean value
result1 = [item[1] >= 20 for item in items]
print(result1)
# to find the list we need to write this

list_of = [item for item in items if item[1] >= 20]
print(list_of)
