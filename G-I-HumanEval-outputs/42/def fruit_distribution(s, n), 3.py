
def fruit_distribution(s, n):
    fruits = s.split()
    apples = int(fruits[0]) if 'apples' in s else 0
    oranges = int(fruits[-2]) if 'oranges' in s else 0
    
    return n - apples - oranges

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```
