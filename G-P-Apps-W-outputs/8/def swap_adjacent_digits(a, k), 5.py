
def swap_adjacent_digits(a, k):
    a_str = str(a)
    a_list = list(a_str)
    n = len(a_list)
    
    for i in range(n):
        max_idx = -1
        for j in range(i+1, min(i+k+1, n)):
            if a_list[j] > a_list[i]:
                if max_idx == -1 or a_list[j] >= a_list[max_idx]:
                    max_idx = j
        if max_idx != -1:
            digit = a_list.pop(max_idx)
            a_list.insert(i, digit)
            k -= (max_idx - i)
            if k == 0:
                break
    
    return int(''.join(a_list))

a, k = map(int, input().split())
print(swap_adjacent_digits(a, k))
```
