
def is_multiple_of_9(N):
    sum_of_digits = sum(int(digit) for digit in str(N))
    if sum_of_digits % 9 == 0:
        return "Yes"
    else:
        return "No"

N = int(input())
print(is_multiple_of_9(N))
```
