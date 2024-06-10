
from itertools import combinations

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(3, n + 1):
        for c in combinations(a, i):
            if c == c[::-1]:
                print("YES")
                break
        else:
            continue
        break
    else:
        print("NO")

