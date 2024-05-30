
def guess_sum_parity(N):
    if N % 2 == 0:
        return "Even"
    else:
        return "Odd"

N = int(input())
if N == 1:
    print("Either")
else:
    print(guess_sum_parity(N))
```
