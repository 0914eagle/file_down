
def can_get_single_element(n, arr):
    max_count = max(arr.count(x) for x in set(arr))
    return "YES" if max_count >= (n + 1) // 2 else "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_get_single_element(n, arr))
