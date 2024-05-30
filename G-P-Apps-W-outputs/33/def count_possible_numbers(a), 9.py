
def count_possible_numbers(a):
    a = list(map(int, str(a)))
    nines_count = 0
    result = 1

    for digit in a:
        if digit == 9:
            nines_count += 1
        else:
            result *= nines_count + 1
            nines_count = 0

    return result

# Input
a = int(input().strip())

# Output
print(count_possible_numbers(a))
```
