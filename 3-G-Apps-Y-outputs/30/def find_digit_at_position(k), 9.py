
def find_digit_at_position(k):
    current_block = 1
    current_position = 1
    while True:
        block_size = len(str(current_block))
        if current_position + block_size < k:
            current_position += block_size
            current_block += 1
        else:
            return int(str(current_block)[k - current_position - 1])

q = int(input())
queries = [int(input()) for _ in range(q)]

for query in queries:
    print(find_digit_at_position(query))
