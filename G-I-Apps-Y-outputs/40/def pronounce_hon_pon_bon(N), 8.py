
def pronounce_hon_pon_bon(N):
    last_digit = N % 10
    if last_digit in [2, 4, 5, 7, 9]:
        print("hon")
    elif last_digit in [0, 1, 6, 8]:
        print("pon")
    else:
        print("bon")

N = int(input())
pronounce_hon_pon_bon(N)
```
