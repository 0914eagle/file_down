
def derivative(xs: list):
    return [i * xs[i] for i in range(1, len(xs))]

print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
