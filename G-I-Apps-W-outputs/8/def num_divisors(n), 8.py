
from math import isqrt

def num_divisors(n):
    count = 0
    for i in range(1, isqrt(n)+1):
        if n % i == 0:
            count += 2
            if i == n // i:
                count -= 1
        if count > 7:
            return 8
    return count

def is_square(num):
    return isqrt(num)**2 == num

def shortest_subsequence_product(arr):
    n = len(arr)
    if n == 1:
        return 1 if is_square(arr[0]) else -1
    
    subseq_lengths = [float('inf')] * n
    for i in range(n):
        if is_square(arr[i]):
            subseq_lengths[i] = 1
            break

    for i in range(n):
        for j in range(i):
            if num_divisors(arr[i]*arr[j]) <= 7:
                subseq_lengths[i] = min(subseq_lengths[i], subseq_lengths[j] + 1)
    
    min_length = min(subseq_lengths)
    return min_length if min_length != float('inf') else -1

# Input
n = int(input())
a = list(map(int, input().split()))

# Output
print(shortest_subsequence_product(a))
```
