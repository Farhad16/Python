leters = ["a", "b", "c"]
zeros = [0] * 10
# list in list
matrix = [[1, 2], [4, 5]]
# list is iteratble
for lists in matrix:
    print(lists)
    for i in lists:
        print(i)
print(zeros)
# list are also can combine

combined = zeros + leters
print(combined)

# range of lists
numbers = list(range(1, 21))
print(numbers)
# length of list
print(len(numbers))

# string as a list
strings = list("Hello Farhad")
print(strings)
