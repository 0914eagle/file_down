
def find_digit_at_position(k):
    n = 1
    while True:
        total_digits = n * (n + 1) // 2
        if total_digits >= k:
            break
        n += 1
    
    offset = total_digits - n
    block_start = offset + 1
    block_end = total_digits
    position_in_block = k - offset
    
    return int(str(n)[position_in_block - 1])

# Read the number of queries
q = int(input())

# Process each query
for _ in range(q):
    k = int(input())
    result = find_digit_at_position(k)
    print(result)
