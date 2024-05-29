
from math import sqrt

def is_square(num):
    return num > 0 and int(sqrt(num)) ** 2 == num

def shortest_subsequence_product_square(n, arr):
    divisors = [0] * (10**6 + 1)
    ans = float('inf')
    for num in arr:
        div = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                cnt = 0
                while num % i == 0:
                    num //= i
                    cnt += 1
                div *= (2 * cnt + 1)
            if num == 1:
                break
        if num > 1:
            div *= 3
        count = divisors[num]
        if count > 0:
            ans = min(ans, count + 1)
            divisors[num] = min(count + 1, div)
        divisors[num] = max(divisors[num], div)
    return -1 if ans == float('inf') else ans

n = int(input())
arr = list(map(int, input().split()))
print(shortest_subsequence_product_square(n, arr))
```
