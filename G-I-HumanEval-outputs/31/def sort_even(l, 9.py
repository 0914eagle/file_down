
def sort_even(l: list):
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    even_indices.sort()
    result = l.copy()
    for i in range(len(l)):
        if i % 2 == 0:
            result[i] = even_indices.pop(0)
    return result

print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
