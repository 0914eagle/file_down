
def find_digit_at_position(k):
    current_block = 1
    current_position = 1

    while True:
        block_size = len(str(current_block))
        if k <= block_size:
            return int(str(current_block)[k - 1])
        else:
            k -= block_size
            current_position += block_size
            current_block += 1

q = int(input())
queries = [int(input()) for _ in range(q)]

for k in queries:
    print(find_digit_at_position(k))
