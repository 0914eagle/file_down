
n = int(input())
e = 0
factorial = 1
for i in range(n+1):
    factorial *= i
    e += 1/factorial
print(e)

