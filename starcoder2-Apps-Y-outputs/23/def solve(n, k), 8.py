
def solve(n, k):
    i = 1
    while k > 0:
        if i % n != 0:
            k -= 1
        i += 1
    return i - 1

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))

