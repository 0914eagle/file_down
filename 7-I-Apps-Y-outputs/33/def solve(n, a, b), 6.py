
import sys

def solve(n, a, b):
    # Complete this function
    return "".join(sorted(set(chr(ord('a') + i) for i in range(n)) * b))[:n]


t = int(input().strip())
for a0 in range(t):
    n, a, b = input().strip().split(' ')
    n, a, b = [int(n), int(a), int(b)]
    result = solve(n, a, b)
    print(result)

