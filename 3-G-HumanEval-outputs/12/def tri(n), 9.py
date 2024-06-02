
def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 1]
    
    result = [3, 1]
    for i in range(2, n+1):
        if i % 2 == 0:
            result.append(1 + i // 2)
        else:
            result.append(result[i-1] + result[i-2] + result[i-3])
    
    return result

# Test the function
print(tri(3))  # Output: [3, 1, 2, 8]
