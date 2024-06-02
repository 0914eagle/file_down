
def find_digit_at_position(k):
    n = 1
    while k > n * (n + 1) // 2:
        k -= n * (n + 1) // 2
        n += 1
    block_start = n * (n - 1) // 2 + 1
    block_number = (k - 1) // n
    position_in_block = (k - 1) % n
    number = block_start + block_number
    return int(str(number)[position_in_block])

# Read the number of queries
q = int(input())

# Process each query
for _ in range(q):
    k = int(input())
    result = find_digit_at_position(k)
    print(result)
