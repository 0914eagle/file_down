
def min_operations(a, b):
    def find_divisors(n):
        divisors = []
        for i in range(2, 6):
            while n % i == 0:
                n /= i
                divisors.append(i)
        return divisors
    
    divisors_a = find_divisors(a)
    divisors_b = find_divisors(b)
    
    if divisors_a != divisors_b:
        return -1
    
    return abs(len(divisors_a) - len(divisors_b))

# Input
a, b = map(int, input().split())

# Output
print(min_operations(a, b))
```
