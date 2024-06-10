
import sys
n = sys.stdin.readline().strip()
k = int(sys.stdin.readline().strip())

def count_ones(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def solve(num, ops):
    if num == 1:
        return ops == k
    if ops > k:
        return False
    res = 0
    while num:
        res += solve(num & (num - 1), ops + 1)
        num >>= 1
    return res

print(solve(int(n, 2), 0) % (10**9 + 7))

