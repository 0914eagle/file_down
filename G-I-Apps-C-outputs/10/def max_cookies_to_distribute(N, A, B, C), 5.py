
def max_cookies_to_distribute(N, A, B, C):
    cookies = [A,B,C]
    cookies.sort(reverse=True)
    
    total_cookies = 0
    while N > 0:
        for i in range(3):
            if cookies[i] == 0:
                continue
            total_cookies += 1
            cookies[i] -= 1
            N -= 1
            if N == 0:
                break
    return total_cookies

# Input
N, A, B, C = map(int, input().split())

# Output
print(max_cookies_to_distribute(N, A, B, C))
```
