
def is_multiple_of_9(N):
    digit_sum = sum(int(digit) for digit in str(N))
    if digit_sum % 9 == 0:
        print("Yes")
    else:
        print("No")

N = int(input().strip())
is_multiple_of_9(N)
```
