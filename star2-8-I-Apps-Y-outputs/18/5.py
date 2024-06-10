
def factorial(n):
result = 1
for i in range(1, n+1):
result *= i
return result

n = int(input())
e = 0
for i in range(n+1):
e += 1 / factorial(i)

print(e)

