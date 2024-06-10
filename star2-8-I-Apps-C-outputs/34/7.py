
import sys
n = int(sys.stdin.readline())
s = set()
for i in range(n):
    s.add(int(sys.stdin.readline()))
max_d = -1
for a in s:
    for b in s:
        for c in s:
            if a + b + c > max_d and a + b + c in s and a != b and a != c and b != c:
                max_d = a + b + c
if max_d == -1:
    print("no solution")
else:
    print(max_d)

