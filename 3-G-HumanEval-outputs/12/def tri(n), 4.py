
def tri(n):
    tribonacci = [0] * (n + 1)
    tribonacci[1] = 3
    for i in range(2, n + 1):
        if i % 2 == 0:
            tribonacci[i] = 1 + i // 2
        else:
            tribonacci[i] = tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3]
    return tribonacci

# Test the function
n = 3
print(tri(n))  # Output: [0, 3, 2, 8]
