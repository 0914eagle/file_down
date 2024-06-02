
def find_digit_at_position(k):
    n = 1
    while True:
        total_digits = n * (n + 1) // 2
        if total_digits >= k:
            break
        n += 1
    
    position_in_block = k - (n - 1) * n // 2
    return int(str(position_in_block)[position_in_block - 1])

q = int(input())
queries = [int(input()) for _ in range(q)]

for query in queries:
    print(find_digit_at_position(query))
