
def get_odd_collatz(n):
    collatz_seq = [n]
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        collatz_seq.append(n)
    
    odd_numbers = sorted(set(collatz_seq) & set(filter(lambda x: x % 2 != 0, collatz_seq)))
    return odd_numbers

# Test the function
print(get_odd_collatz(5))  # Output: [1, 5]
