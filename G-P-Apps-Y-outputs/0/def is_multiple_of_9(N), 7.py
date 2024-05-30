
def is_multiple_of_9(N):
    digit_sum = sum(int(d) for d in str(N))
    return "Yes" if digit_sum % 9 == 0 else "No"

N = int(input())
print(is_multiple_of_9(N))
```
