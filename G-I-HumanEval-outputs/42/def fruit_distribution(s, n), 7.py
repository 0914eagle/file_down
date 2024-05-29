
def fruit_distribution(s, n):
    apples = 0
    oranges = 0
    
    # Split the input string to extract the number of apples and oranges
    for word in s.split():
        if word.isnumeric():
            if "apples" in s:
                apples = int(word)
            elif "oranges" in s:
                oranges = int(word)
    
    # Calculate the number of mango fruits
    mangoes = n - apples - oranges
    return mangoes

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))    # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
