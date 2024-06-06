
# python3
from random import randint, seed

seed(12431421)

n = randint(3, 1000)
print(n)

for i in range(n):
    print(" ".join(map(str, [randint(0, 1000000000) for _ in range(n)])))

