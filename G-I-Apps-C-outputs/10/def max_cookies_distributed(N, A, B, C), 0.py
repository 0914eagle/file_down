
def max_cookies_distributed(N, A, B, C):
    total_cookies = A + B + C
    max_cookies = min(total_cookies, (N // 2) * 2)
    return max_cookies

# Reading input
N, A, B, C = map(int, input().split())

# Calculate and print the maximum number of cookies distributed
print(max_cookies_distributed(N, A, B, C))
```
