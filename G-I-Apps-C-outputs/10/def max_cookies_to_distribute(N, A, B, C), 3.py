
def max_cookies_to_distribute(N, A, B, C):
    total_cookies = A + B + C
    if N == 2:
        return total_cookies
    max_same_kind = max(A, B, C)
    remaining_cookies = total_cookies - max_same_kind
    return max_same_kind + min(remaining_cookies, N - 2)

# Input parsing
N, A, B, C = map(int, input().split())

# Call the function and print the result
print(max_cookies_to_distribute(N, A, B, C))
```
