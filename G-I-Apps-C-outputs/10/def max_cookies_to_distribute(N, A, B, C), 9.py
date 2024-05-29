
def max_cookies_to_distribute(N, A, B, C):
    sum_cookies = A + B + C
    max_same_type = max(max(A, B, C), (sum_cookies - max(A, B, C)))
    remaining_cookies = sum_cookies - max_same_type
    max_distributed_cookies = min(remaining_cookies, N) * 2 + min(remaining_cookies - min(remaining_cookies, N), N - 1)
    
    return max_distributed_cookies

# Input reading and function call
N, A, B, C = map(int, input().split())
result = max_cookies_to_distribute(N, A, B, C)
print(result)
```
