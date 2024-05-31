
def can_make_change(a, b, n, S):
    if S % n <= b and (S - (S % n)) // n <= a:
        return "YES"
    else:
        return "NO"

# Read input
q = int(input())
for _ in range(q):
    a, b, n, S = map(int, input().split())
    print(can_make_change(a, b, n, S))
