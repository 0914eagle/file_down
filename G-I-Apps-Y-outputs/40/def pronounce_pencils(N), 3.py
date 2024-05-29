
def pronounce_pencils(N):
    last_digit = N % 10
    if last_digit in [0, 1, 6, 8]:
        print("pon")
    elif last_digit == 3:
        print("bon")
    else:
        print("hon")

# Sample Input
N = 16
pronounce_pencils(N)
```
