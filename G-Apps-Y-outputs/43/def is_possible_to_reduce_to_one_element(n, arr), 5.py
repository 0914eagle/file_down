
def is_possible_to_reduce_to_one_element(n, arr):
    count_map = {}
    for num in arr:
        if num not in count_map:
            count_map[num] = 1
        else:
            count_map[num] += 1
    
    max_count = max(count_map.values())
    
    if max_count > len(arr) // 2:
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = is_possible_to_reduce_to_one_element(n, arr)
    print(result)
