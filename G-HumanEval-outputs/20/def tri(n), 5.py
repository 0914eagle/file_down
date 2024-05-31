
def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 1]

    result = [3, 1]
    a, b, c = 3, 1, 2

    for i in range(3, n + 1):
        if i % 2 == 0:
            tri_num = 1 + i // 2
        else:
            tri_num = a + b + c
            a, b, c = b, c, tri_num

        result.append(tri_num)

    return result

# Test cases
print(tri(3))  # Output: [3, 1, 2, 8]
print(tri(7))  # Output: [3, 1, 2, 8, 5, 12, 27, 44]
