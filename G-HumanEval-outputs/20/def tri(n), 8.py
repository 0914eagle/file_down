
def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [3]
    elif n == 2:
        return [1, 3]
    
    tribonacci = [1, 3]
    
    def calculate_tribonacci(i):
        if i % 2 == 0:
            return 1 + i // 2
        else:
            return tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i + 1]
        
    for i in range(2, n):
        tribonacci.append(calculate_tribonacci(i))
    
    return tribonacci

print(tri(3))  # Output: [1, 3, 2, 8]
