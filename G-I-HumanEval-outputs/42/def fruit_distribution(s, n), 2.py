
def fruit_distribution(s, n):
    # Separate the numbers of apples and oranges from the input string
    fruits = s.split()
    apples = int(fruits[0])
    oranges = int(fruits[3])
    
    # Calculate the number of mango fruits in the basket
    mango = n - apples - oranges
    
    return mango

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
