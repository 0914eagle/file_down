
def max_cookies_distributed(N, A, B, C):
    if A == 0 and B == 0 and C == 0:
        return 0

    num_cookies = A + B + C
    max_cookies = min(num_cookies, N // 2 * 2)
    return max_cookies

# Input parsing
N, A, B, C = map(int, input().split())

# Call the function and print the result
print(max_cookies_distributed(N, A, B, C))
```
