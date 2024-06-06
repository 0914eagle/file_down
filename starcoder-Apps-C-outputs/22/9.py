
import random
import math

n = random.randint(2,100000)
m = random.randint(1,100000)
h = random.randint(2,100000)

print(n, m, h)

for _ in range(n):
    print(random.randint(0,h-1), end=' ')
print()

for _ in range(m):
    x = random.randint(1,n)
    y = random.randint(1,n)
    while x==y:
        y = random.randint(1,n)
    print(x,y)
