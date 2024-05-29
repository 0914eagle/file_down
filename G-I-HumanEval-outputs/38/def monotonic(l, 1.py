
def monotonic(l: list):
    is_increasing = all(l[i] <= l[i + 1] for i in range(len(l) - 1))
    is_decreasing = all(l[i] >= l[i + 1] for i in range(len(l) - 1))
    
    return is_increasing or is_decreasing

print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
