
def can_reduce_to_one_element(n, arr):
    max_freq = max(arr.count(i) for i in set(arr))
    return max_freq >= len(arr) - max_freq

# Input reading
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    # Check if it is possible to reduce to one element
    result = "YES" if can_reduce_to_one_element(n, arr) else "NO"
    print(result)
