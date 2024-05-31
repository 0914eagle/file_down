
def can_reduce_to_one_element(n, arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            
    max_count = max(count.values())
    
    if max_count > (n - max_count):
        return "NO"
    else:
        return "YES"

# Input reading
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = can_reduce_to_one_element(n, arr)
    print(result)
