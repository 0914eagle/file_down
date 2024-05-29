
def max_cookies_to_distribute(N, A, B, C):
    cookies = [A, B, C]
    total_cookies = sum(cookies)
    max_cookies = 0
    
    for _ in range(N):
        max_cookie_index = cookies.index(max(cookies))
        
        if max_cookie_index == 0:
            if A > 0:
                max_cookies += 1
                A -= 1
            elif B > 0:
                max_cookies += 1
                B -= 1
            else:
                break
        elif max_cookie_index == 1:
            if B > 0:
                max_cookies += 1
                B -= 1
            elif A > 0:
                max_cookies += 1
                A -= 1
            else:
                break
        elif max_cookie_index == 2:
            if C > 0:
                max_cookies += 1
                C -= 1
            else:
                break
    
    return max_cookies

# Read input
N, A, B, C = map(int, input().split())

# Call the function and print the output
print(max_cookies_to_distribute(N, A, B, C))
```
