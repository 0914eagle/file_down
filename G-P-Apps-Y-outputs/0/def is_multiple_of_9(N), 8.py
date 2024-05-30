
def is_multiple_of_9(N):
    if N == 0:
        return "Yes"
    
    digit_sum = 0
    while N > 0:
        digit_sum += N % 10
        N //= 10
    
    return "Yes" if digit_sum % 9 == 0 else "No"

N = int(input())
print(is_multiple_of_9(N))
```
