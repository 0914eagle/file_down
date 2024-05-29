
def max_cookies_distributed(N, A, B, C):
    cookies = [A, B, C]
    cookies.sort(reverse=True)
    
    if cookies[0] > (cookies[1] + cookies[2] + 1):
        return cookies[1] + cookies[2] + 1
    
    total = min((cookies[0] + cookies[1] + cookies[2] + 1), N)
    return total

# Reading input
N, A, B, C = map(int, input().split())

# Calculating and printing output
print(max_cookies_distributed(N, A, B, C))
```
