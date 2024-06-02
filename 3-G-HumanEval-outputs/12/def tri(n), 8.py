
def tri(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 1]
    
    tribonacci = [3, 1, 2]
    for i in range(3, n + 1):
        if i % 2 == 0:
            tribonacci.append(1 + i // 2)
        else:
            tribonacci.append(tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3])
    
    return tribonacci

# Test the function
print(tri(3))  # Output: [3, 1, 2, 6]
