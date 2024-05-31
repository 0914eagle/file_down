
def can_reduce_to_single_element(n, arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    max_freq = max(freq.values())
    if max_freq >= n - 1:
        return "YES"
    if n % 2 == 0 and max_freq >= n // 2:
        return "YES"
    
    return "NO"

# Input reading
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = can_reduce_to_single_element(n, arr)
    print(result)
