
def can_make_change(a, b, n, S):
    max_x = min(a, S // n)
    if max_x * n + b >= S:
        return "YES"
    else:
        return "NO"

q = int(input())
for _ in range(q):
    a, b, n, S = map(int, input().split())
    print(can_make_change(a, b, n, S))
