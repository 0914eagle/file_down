
def monotonic(l: list):
    increasing = all(l[i] <= l[i + 1] for i in range(len(l) - 1))
    decreasing = all(l[i] >= l[i + 1] for i in range(len(l) - 1))
    
    return increasing or decreasing

print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
