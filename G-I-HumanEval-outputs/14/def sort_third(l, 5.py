
def sort_third(l: list):
    result = l.copy()
    for i in range(len(l)):
        if i % 3 == 0:
            result[i] = l[i]
    for i in range(len(l) // 3):
        subset = sorted(l[i * 3: (i+1) * 3])
        for j, val in zip(range(i * 3, (i+1) * 3), subset):
            result[j] = val
    return result

# Test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
