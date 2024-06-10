
from itertools import permutations

x = input()
digits = [int(d) for d in x]
n = len(digits)

for i in range(1, n+1):
    for perm in permutations(digits, i):
        num = int(''.join(map(str, perm)))
        if num > int(x):
            print(num)
            break
    else:
        continue
    break
else:
    print(0)

