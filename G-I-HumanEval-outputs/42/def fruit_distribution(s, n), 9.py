
def fruit_distribution(s, n):
    
    total_apples = 0
    total_oranges = 0
    
    # Extract the count of apples and oranges from the input string
    words = s.split()
    for i in range(len(words) - 1):
        if words[i].isdigit():
            if words[i + 1] == "apples":
                total_apples = int(words[i])
            elif words[i + 1] == "oranges":
                total_oranges = int(words[i])
    
    return n - total_apples - total_oranges

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```
