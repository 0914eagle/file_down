
def find_digit_at_position(k):
    n = 1
    while k > n * (n + 1) // 2:
        k -= n * (n + 1) // 2
        n += 1

    block_start = n * (n - 1) // 2 + 1
    block_num = (k - 1) // n
    num_in_block = (k - 1) % n

    num = block_start + block_num
    return int(str(num)[num_in_block])

# Read the number of queries
q = int(input())

# Process each query
for _ in range(q):
    k = int(input())
    result = find_digit_at_position(k)
    print(result)
