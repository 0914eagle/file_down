
def solve_sliding_blocks(N, M, B, blocks):
    initial_board = [[0] * M for _ in range(N)]
    for r, c in blocks:
        initial_board[r-1][c-1] = 1

    moves = []
    for r, c in blocks[1:]:
        while r > 1:
            moves.append((r-1, '^'))
            r -= 1
        while c > 1:
            moves.append((c-1, '<'))
            c -= 1

    if len(moves) != B - 1:
        return "impossible"
    else:
        result = "possible\n"
        for move in moves:
            result += f"{move[1]} {move[0]}\n"
        return result

# Input parsing
N, M, B = map(int, input().split())
blocks = [tuple(map(int, input().split())) for _ in range(B)]

# Call the function and print the result
print(solve_sliding_blocks(N, M, B, blocks))
```
