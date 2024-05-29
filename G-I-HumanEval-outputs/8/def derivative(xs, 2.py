
def derivative(xs: list):
    return [i * c for i, c in enumerate(xs[1:], 1)]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
