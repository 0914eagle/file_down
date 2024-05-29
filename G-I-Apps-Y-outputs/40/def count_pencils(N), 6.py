
def count_pencils(N):
    last_digit = N % 10
    if last_digit in [2, 4, 5, 7, 9]:
        return "hon"
    elif last_digit in [0, 1, 6, 8]:
        return "pon"
    elif last_digit == 3:
        return "bon"

# Read input
N = int(input().strip())

# Get the pronunciation of "本"
pronunciation = count_pencils(N)

print(pronunciation)
```
