
def eat(number, need, remaining):
    total_eaten = number + min(need, remaining)
    carrots_left = max(0, remaining - need)
    return [total_eaten, carrots_left]

# Test cases
print(eat(5, 6, 10))  # Output: [11, 4]
print(eat(4, 8, 9))   # Output: [12, 1]
print(eat(1, 10, 10))  # Output: [11, 0]
print(eat(2, 11, 5))   # Output: [7, 0]
```
