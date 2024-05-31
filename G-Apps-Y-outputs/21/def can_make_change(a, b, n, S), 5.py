
def can_make_change(a, b, n, S):
    for x in range(a + 1):
        if x * n <= S and (S - x * n) <= b:
            return "YES"
    return "NO"

# Input
q = int(input())
for _ in range(q):
    a, b, n, S = map(int, input().split())
    print(can_make_change(a, b, n, S))
