
def eat(number, need, remaining):
    total_eaten = number + min(need, remaining)
    left_over = max(0, remaining - need)
    return [total_eaten, left_over]

# Test cases
print(eat(5, 6, 10))  # [11, 4]
print(eat(4, 8, 9))   # [12, 1]
print(eat(1, 10, 10))  # [11, 0]
print(eat(2, 11, 5))   # [7, 0]
```
