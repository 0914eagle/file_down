
def solve_sliding_blocks(N, M, B, blocks):
    initial_block = blocks[0]
    target_blocks = blocks[1:]

    moves = []
    curr_row = initial_block[0]
    curr_col = initial_block[1]

    for target_block in target_blocks:
        target_row = target_block[0]
        target_col = target_block[1]

        while curr_row > target_row:
            moves.append(f'v {curr_row}')
            curr_row -= 1

        while curr_row < target_row:
            moves.append(f'^ {curr_row + 1}')
            curr_row += 1

        while curr_col > target_col:
            moves.append(f'< {curr_col}')
            curr_col -= 1

        while curr_col < target_col:
            moves.append(f'> {curr_col + 1}')
            curr_col += 1

    if len(moves) == B - 1:
        print("possible")
        for move in moves:
            print(move)
    else:
        print("impossible")

# Input parsing
N, M, B = map(int, input().split())
blocks = []
for _ in range(B):
    r, c = map(int, input().split())
    blocks.append((r, c))

# Solve the sliding blocks puzzle
solve_sliding_blocks(N, M, B, blocks)
```
