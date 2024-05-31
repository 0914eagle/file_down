
def below_threshold(l: list, t: int):
    
    return all(num < t for num in l)

# Testing the function
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
