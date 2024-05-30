
def swap_digits(num, k):
    num_str = str(num)
    num_list = list(num_str)
    
    for i in range(len(num_list)):
        max_idx = i
        for j in range(i+1, min(i+k+1, len(num_list))):
            if num_list[j] > num_list[max_idx]:
                max_idx = j
        
        for j in range(max_idx, i, -1):
            num_list[j], num_list[j-1] = num_list[j-1], num_list[j]
            k -= 1
            if k == 0:
                break
        
        if k == 0:
            break
    
    return int(''.join(num_list))

a, k = map(int, input().split())
print(swap_digits(a, k))
```
