
k = int(input())

def isPerfect(n):
  sum_digits = 0
  while n > 0:
    sum_digits += n % 10
    n //= 10
  return sum_digits == 10

count = 0
i = 0
while count < k:
  i += 1
  if isPerfect(i):
    count += 1

print(i)

