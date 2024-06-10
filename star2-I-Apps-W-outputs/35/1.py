
def solve(k, a):
    n = sum(a)
    if k % n != 0:
        return -1
    d = k // n
    return 7 * d

t = int(input())
for _ in range(t):
    k = int(input())
    a = list(map(int, input().split()))
    print(solve(k, a))

