try:
    age = int(input("Age "))
except ValueError:
    print("You didn't enter a valid age: ")

else:
    print("No exception")
print("Execution continues")
