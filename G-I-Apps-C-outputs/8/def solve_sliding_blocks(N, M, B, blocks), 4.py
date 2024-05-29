
def solve_sliding_blocks(N, M, B, blocks):
    start_row, start_col = blocks[0]
    moves = []
    
    def add_move(move, k):
        moves.append(f"{move} {k}")

    for block in blocks[1:]:
        end_row, end_col = block
        # Move rows
        while start_row < end_row:
            add_move("v", start_row)
            start_row += 1
        while start_row > end_row:
            add_move("^", start_row)
            start_row -= 1

        # Move columns
        while start_col < end_col:
            add_move(">", start_col)
            start_col += 1
        while start_col > end_col:
            add_move("<", start_col)
            start_col -= 1
    
    return moves

# Input parsing
N, M, B = map(int, input().split())
blocks = [tuple(map(int, input().split())) for _ in range(B)]

moves = solve_sliding_blocks(N, M, B, blocks)

if len(moves) == B - 1:
    print("possible")
    for move in moves:
        print(move)
else:
    print("impossible")
```
