
import math

def is_perfect_square(num):
    sqrt_num = int(math.sqrt(num))
    return num == sqrt_num * sqrt_num

def shortest_subsequence_with_perfect_square_product(n, arr):
    ans = float('inf')
    for mask in range(1, 2**n):
        product = 1
        count = 0
        for i in range(n):
            if (mask >> i) & 1:
                product *= arr[i]
                count += 1
        if is_perfect_square(product):
            ans = min(ans, count)
    return ans if ans != float('inf') else -1

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Output
print(shortest_subsequence_with_perfect_square_product(n, arr))
