
def min_xor_value(n, a):
    min_val = float('inf')
    
    for i in range(31, -1, -1):
        prefix_set = set()
        new_min = min_val | (1 << i)
        
        for num in a:
            prefix_set.add(num >> i)
        
        for prefix in prefix_set:
            if (new_min ^ prefix) in prefix_set:
                min_val = new_min
                break
    
    return min_val

# Reading input
n = int(input())
a = list(map(int, input().split()))

# Calling the function and printing the result
print(min_xor_value(n, a))
```
