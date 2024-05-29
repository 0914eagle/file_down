
def max_cookies_to_distribute(N, A, B, C):
    total_cookies = A + B + C
    remaining_friends = N - 2
    if remaining_friends <= 0:
        return total_cookies
    
    max_cookies = min(total_cookies, total_cookies // remaining_friends)

    return max_cookies

# Input parsing
inputs = list(map(int, input().split()))
N, A, B, C = inputs[0], inputs[1], inputs[2], inputs[3]

# Call the function and output the result
print(max_cookies_to_distribute(N, A, B, C))
```
