
def can_make_change(a, b, n, S):
    if S % n > a or S > a * n + b:
        return "NO"
    return "YES"

q = int(input())
for _ in range(q):
    a, b, n, S = map(int, input().split())
    print(can_make_change(a, b, n, S))
