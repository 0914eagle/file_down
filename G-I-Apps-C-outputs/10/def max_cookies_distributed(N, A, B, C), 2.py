
def max_cookies_distributed(N, A, B, C):
    total_cookies = A + B + C
    
    if N == 2:
        return min(total_cookies, N)
    
    max_same_type = max(A, B, C)
    total_same_type = A + B + C - max_same_type
    
    if max_same_type >= total_same_type + 2:
        return min(total_cookies, 2*N)
    else:
        return min(total_cookies, total_same_type + max_same_type + 1)

# Input parsing
input_values = input().split()
N = int(input_values[0])
A = int(input_values[1])
B = int(input_values[2])
C = int(input_values[3])

result = max_cookies_distributed(N, A, B, C)
print(result)
```
