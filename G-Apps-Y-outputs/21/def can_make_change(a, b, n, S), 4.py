
def can_make_change(a, b, n, S):
    for x in range(a+1):
        for y in range(b+1):
            if x*n + y == S:
                return "YES"
    return "NO"

q = int(input())
for _ in range(q):
    a, b, n, S = map(int, input().split())
    print(can_make_change(a, b, n, S))
