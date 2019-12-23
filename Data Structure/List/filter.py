items = [
    ("Product1", 10),
    ("Product2", 25),
    ("Product3", 20)
]
x = list(filter(lambda item: item[1] >= 15, items))
print(x)
