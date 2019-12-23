from sys import getsizeof
values = (x * 2 for x in range(1000000))
print(getsizeof(values))

values = [x * 2 for x in range(100)]
print(getsizeof(values))
