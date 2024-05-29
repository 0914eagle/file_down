
def get_odd_collatz(n):
    result = [n]
    while n != 1:
        if n % 2 == 0:  # If even
            n = n // 2
        else:            # If odd
            n = 3 * n + 1
        result.append(n)
    
    return sorted(set(result) & set(filter(lambda x: x % 2 != 0, result)))

# Test the function
print(get_odd_collatz(5))  # Output: [1, 5]
