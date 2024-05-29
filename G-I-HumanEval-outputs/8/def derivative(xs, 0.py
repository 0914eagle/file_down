 

def derivative(xs: list):
    return [xs[i] * i for i in range(1, len(xs))]

# Test cases 
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]

