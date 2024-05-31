
def can_obtain_single_element_array(n, arr):
    freq_map = {}
    for num in arr:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    
    max_freq = max(freq_map.values())
    total = sum(freq_map.values())
    
    if max_freq >= (total + 1) // 2:
        return "YES"
    else:
        return "NO"
    
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = can_obtain_single_element_array(n, arr)
    print(result)
