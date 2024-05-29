
def count_pencils(number):
    last_digit = number % 10
    if last_digit in [2, 4, 5, 7, 9]:
        return "hon"
    elif last_digit in [0, 1, 6, 8]:
        return "pon"
    else:
        return "bon"

# Input
N = int(input())

# Output
print(count_pencils(N))
```
