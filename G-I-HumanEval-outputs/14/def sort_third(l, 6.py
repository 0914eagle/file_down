
def sort_third(l: list):
    divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    sorted_divisible_by_three = sorted(divisible_by_three)
    result = []
    for i in range(len(l)):
        if i % 3 == 0:
            result.append(sorted_divisible_by_three.pop(0))
        else:
            result.append(l[i])
    return result

print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
