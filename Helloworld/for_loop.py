successfull = False
for number in range(3):
    print("Attempt", number ,(number)*".")
    if successfull:
        print("Successful")
        break
else:
    print("Loop is attempt 3 Times")