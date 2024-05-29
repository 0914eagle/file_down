
from math import isqrt

def is_perfect_square(num):
    return isqrt(num) ** 2 == num

def num_divisors(num):
    count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if num // i == i:
                count += 1
            else:
                count += 2
        if count > 7:
            return 8
    return count

def shortest_subsequence_length(n, arr):
    dp = []
    for i in range(n):
        if num_divisors(arr[i]) > 7:
            continue
        for j in range(len(dp)):
            if is_perfect_square(dp[j] * arr[i]):
                dp.append(dp[j] * arr[i])
        dp.append(arr[i])
    
    if not dp:
        return -1
    return len(min(dp, key=len))

# Input reading from stdin, call the function, and print the result
n = int(input())
arr = list(map(int, input().split()))
result = shortest_subsequence_length(n, arr)
print(result)
```
