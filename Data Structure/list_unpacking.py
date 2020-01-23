numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# unpacking and packing also

first, second, *others = numbers
print(first, second)  # print the first and second element
print(others)  # print the rest of the elements

# pack a numbers of elements into list using arbitary arguments


def packing(*number):
    print(number)


lists = [1, 2, 3, 4, 5]


packing(1, 2, 3, 4, 5, 6, 7, 8)
