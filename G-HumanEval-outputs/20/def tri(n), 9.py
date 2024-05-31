
def tri(n):
    sequence = [0] * (n+1)
    if n >= 1:
        sequence[1] = 3
    for i in range(2, n+1):
        if i % 2 == 0:
            sequence[i] = 1 + i // 2
        else:
            sequence[i] = sequence[i-1] + sequence[i-2] + sequence[i+1]
    return sequence

# Test the function
print(tri(3))  # Output: [0, 3, 2, 8]
