
def count_pronunciation(N):
    last_digit = int(str(N)[-1])
    if last_digit in [2, 4, 5, 7, 9]:
        return "hon"
    elif last_digit in [0, 1, 6, 8]:
        return "pon"
    else:
        return "bon"

# Read input from Standard Input
N = int(input())

# Print the answer
print(count_pronunciation(N))
```
