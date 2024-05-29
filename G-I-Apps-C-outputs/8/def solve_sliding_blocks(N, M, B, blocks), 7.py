
def solve_sliding_blocks(N, M, B, blocks):
    initial_board = set([(1, 1)])  # Assume the block is already at (1, 1) in the initial board
    target_board = set(blocks)
    
    if len(initial_board) + B != len(target_board):
        print("impossible")
        return
    
    moves = []
    
    for block in target_board:
        r, c = block
        while (r, c) not in initial_board:
            if r > 1 and (r-1, c) in target_board:
                moves.append(f"^ {r}")
                r -= 1
            elif r < N and (r+1, c) in target_board:
                moves.append(f"v {r}")
                r += 1
            elif c > 1 and (r, c-1) in target_board:
                moves.append(f"< {c}")
                c -= 1
            elif c < M and (r, c+1) in target_board:
                moves.append(f"> {c}")
                c += 1
    
    print("possible")
    for move in moves:
        print(move)

# Input processing
input_data = input().strip().split()
N, M, B = int(input_data[0]), int(input_data[1]), int(input_data[2])
blocks = []
for _ in range(B):
    r, c = map(int, input().strip().split())
    blocks.append((r, c))

# Solve the sliding blocks puzzle
solve_sliding_blocks(N, M, B, blocks)
```
