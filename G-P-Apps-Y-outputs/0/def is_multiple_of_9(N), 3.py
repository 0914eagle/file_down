
def is_multiple_of_9(N):
    if N == 0:
        return "Yes"
    
    total = sum(int(digit) for digit in str(N))
    
    if total % 9 == 0:
        return "Yes"
    else:
        return "No"

N = int(input())
print(is_multiple_of_9(N))
```
