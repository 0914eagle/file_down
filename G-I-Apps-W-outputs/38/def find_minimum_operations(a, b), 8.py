
def find_minimum_operations(a, b):
    def get_divisible_count(num, divisor):
        count = 0
        while num % divisor == 0:
            num //= divisor
            count += 1
        return count
    
    a_ops = get_divisible_count(a, 2) + get_divisible_count(a, 3) + get_divisible_count(a, 5)
    b_ops = get_divisible_count(b, 2) + get_divisible_count(b, 3) + get_divisible_count(b, 5)
    
    if a == b and a_ops == b_ops:
        return 0
    elif a_ops == b_ops:
        return abs(a_ops - b_ops)
    else:
        return -1

# Input
a, b = map(int, input().split())

# Output
print(find_minimum_operations(a, b))
```
