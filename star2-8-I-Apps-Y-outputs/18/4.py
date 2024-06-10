
def factorial(n):
if n == 0:
return 1
return n * factorial(n - 1)
n = int(input())
e = 0
for i in range(n + 1):
e += 1 / factorial(i)
print(e)

