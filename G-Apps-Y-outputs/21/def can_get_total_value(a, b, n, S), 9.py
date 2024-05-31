
def can_get_total_value(a, b, n, S):
    max_n_coins = min(S // n, a)
    if max_n_coins * n + b >= S:
        return "YES"
    else:
        return "NO"

q = int(input())
for _ in range(q):
    a, b, n, S = map(int, input().split())
    print(can_get_total_value(a, b, n, S))
