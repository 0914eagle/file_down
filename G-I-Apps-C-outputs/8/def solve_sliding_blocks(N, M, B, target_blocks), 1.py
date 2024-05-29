
def solve_sliding_blocks(N, M, B, target_blocks):
    def is_adjacent(block1, block2):
        return abs(block1[0] - block2[0]) + abs(block1[1] - block2[1]) == 1

    if B == 1:
        return "impossible"

    initial_block = target_blocks[0]
    visited = set()
    visited.add(initial_block)
    queue = [initial_block]

    while queue:
        current_block = queue.pop(0)

        for target_block in target_blocks:
            if target_block not in visited and is_adjacent(current_block, target_block):
                visited.add(target_block)
                queue.append(target_block)

    if len(visited) != B:
        return "impossible"
    else:
        moves = []
        for target_block in target_blocks[1:]:
            if target_block[0] > initial_block[0]:
                moves.append(f"v {target_block[1]}")
            elif target_block[0] < initial_block[0]:
                moves.append(f"^ {target_block[1]}")
            elif target_block[1] > initial_block[1]:
                moves.append(f"> {target_block[0]}")
            else:
                moves.append(f"< {target_block[0]}")

        return "possible", moves

# Input
input_data = input().split()
N, M, B = int(input_data[0]), int(input_data[1]), int(input_data[2])
target_blocks = []
for _ in range(B):
    block = tuple(map(int, input().split()))
    target_blocks.append(block)

# Solve
result = solve_sliding_blocks(N, M, B, target_blocks)

# Output
if result == "impossible":
    print("impossible")
else:
    print("possible")
    for move in result[1]:
        print(move)
```
