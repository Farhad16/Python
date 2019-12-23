
x = input("")
n = int(x)
reverse = 0
while n > 0:
    reverse = reverse * 10
    reverse = reverse + (n % 10)
    n = int(n/10)

print(reverse)
