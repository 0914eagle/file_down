
def can_reduce_to_one_element(n, a):
    min_val = min(a)
    max_val = max(a)
    count_min = a.count(min_val)
    count_max = a.count(max_val)
    if max_val - min_val <= 1 or count_min == n or count_max == n:
        return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = can_reduce_to_one_element(n, a)
    print(result)
