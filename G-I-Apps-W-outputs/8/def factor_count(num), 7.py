
import math

def factor_count(num):
    count = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if num / i == i:
                count += 1
            else:
                count += 2
    return count

def shortest_perfect_sq_subsequence(n, arr):
    min_len = float('inf')
    for mask in range(1, 1 << n):
        subseq = []
        for i in range(n):
            if mask & (1 << i):
                subseq.append(arr[i])
        
        product = 1
        for num in subseq:
            product *= num
        
        sqrt_product = int(math.sqrt(product))
        if sqrt_product * sqrt_product == product:
            min_len = min(min_len, len(subseq))
    
    if min_len == float('inf'):
        return -1
    else:
        return min_len

# Input parsing
n = int(input())
arr = list(map(int, input().split()))

result = shortest_perfect_sq_subsequence(n, arr)
print(result)
```
