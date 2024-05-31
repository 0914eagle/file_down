
def can_reduce_to_one_element(n, arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    max_count = max(count.values())
    if n % 2 == 0 and max_count <= n // 2:
        return "YES"
    if n % 2 == 1 and max_count <= n // 2 + 1:
        return "YES"
    
    return "NO"

# Input reading
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_reduce_to_one_element(n, arr))
