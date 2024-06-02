
def find_digit_at_position(k):
    n = 1
    while k > n * (n + 1) // 2:
        k -= n * (n + 1) // 2
        n += 1
    block_start = n * (n - 1) // 2 + 1
    block_number = (k - 1) // n
    position_in_block = (k - 1) % n
    return str(block_start + block_number + position_in_block)

q = int(input())
queries = [int(input()) for _ in range(q)]

for k in queries:
    print(find_digit_at_position(k))
