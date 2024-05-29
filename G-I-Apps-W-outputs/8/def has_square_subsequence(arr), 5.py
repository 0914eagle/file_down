
import math

def has_square_subsequence(arr):
    squares = set()
    for i in range(1, int(1e3)+1):
        squares.add(i*i)

    result = float('inf')
    for mask in range(1, 1 << len(arr)):
        product = 1
        for i in range(len(arr)):
            if (mask >> i) & 1:
                product *= arr[i]

        if math.isqrt(product) ** 2 == product:
            result = min(result, bin(mask).count('1'))

    return result if result != float('inf') else -1

n = int(input())
arr = list(map(int, input().split()))
print(has_square_subsequence(arr))
```
