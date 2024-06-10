
import sys

N = int(sys.stdin.readline())
S = set()
for i in range(N):
    S.add(int(sys.stdin.readline()))

max_sum = -1
for a in S:
    for b in S:
        if a == b:
            continue
        for c in S:
            if a == c or b == c:
                continue
            if a + b + c > max_sum:
                max_sum = a + b + c

if max_sum == -1:
    print("no solution")
else:
    print(max_sum)

