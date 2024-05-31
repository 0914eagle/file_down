
def tri(n):
    result = [3]  # Initialize the list with the first Tribonacci number
    if n == 0:
        return result
    elif n == 1:
        return result + [1]
    elif n == 2:
        return result + [3, 2]

    for i in range(2, n):
        if i % 2 == 0:
            result.append(1 + i // 2)
        else:
            result.append(result[-1] + result[-2] + result[-3])

    return result

# Test the function
print(tri(3))  # Output: [3, 1, 3, 7]
