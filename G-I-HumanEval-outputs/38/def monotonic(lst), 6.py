
def monotonic(lst):
    increasing = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    decreasing = all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
    
    return increasing or decreasing

monotonic([1, 2, 4, 20])  # Output: True
monotonic([1, 20, 4, 10])  # Output: False
monotonic([4, 1, 0, -10])  # Output: True
