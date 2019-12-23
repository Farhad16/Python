def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less than 0")
    return 10 / age


x = int(input("Age "))
try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
