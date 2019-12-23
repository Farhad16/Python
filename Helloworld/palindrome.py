x = input("")
n = int(x)
reverse = 0
for number in range(1, n+1, 1):
    t = number
    while number > 0:
        reverse = reverse * 10
        reverse = reverse + (number % 10)
        t = int(t/10)

    if t == reverse:
        print(reverse)
