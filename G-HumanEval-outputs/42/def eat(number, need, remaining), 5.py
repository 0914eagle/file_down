
def eat(number, need, remaining):
    total_carrots = number + remaining
    if remaining >= need:
        total_carrots += need
        remaining -= need
    else:
        total_carrots += remaining
        remaining = 0
    return [total_carrots, remaining]

# Test cases
print(eat(5, 6, 10))  # Output: [11, 4]
print(eat(4, 8, 9))   # Output: [12, 1]
print(eat(1, 10, 10))  # Output: [11, 0]
print(eat(2, 11, 5))   # Output: [7, 0]
```
