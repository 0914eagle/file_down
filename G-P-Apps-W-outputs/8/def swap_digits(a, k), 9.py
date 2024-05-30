
def swap_digits(a, k):
    a_str = str(a)
    a_list = list(a_str)
    n = len(a_list)
    
    for i in range(n):
        max_index = i
        for j in range(i+1, min(n, i+k+1)):
            if a_list[j] > a_list[max_index]:
                max_index = j
        
        for j in range(max_index, i, -1):
            a_list[j], a_list[j-1] = a_list[j-1], a_list[j]
            k -= 1
            if k == 0:
                break
        
        if k == 0:
            break
    
    return int("".join(a_list))

# Input
a, k = map(int, input().split())

# Output
print(swap_digits(a, k))
```
