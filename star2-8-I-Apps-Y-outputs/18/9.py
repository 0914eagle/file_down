
def euler_number(n):
def factorial(n):
if n == 0:
return 1
else:
return n * factorial(n - 1)

sum = 0
for i in range(n + 1):
sum += 1 / factorial(i)

return sum

