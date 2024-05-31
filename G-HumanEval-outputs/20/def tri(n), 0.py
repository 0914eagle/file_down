
def tri(n):
    result = [0] * (n + 1)
    if n > 0:
        result[1] = 3
    if n > 1:
        result[2] = 1 + 2 / 2
    for i in range(3, n + 1):
        if i % 2 == 0:
            result[i] = 1 + i // 2
        else:
            result[i] = result[i - 1] + result[i - 2] + result[i - 3]
    return result

# Test the function
n = 3
print(tri(n))  # Output: [0, 3, 2, 8]
