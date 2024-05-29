
def solve_sliding_blocks(N, M, B, blocks):
    # Check if the number of blocks is sufficient to cover the entire target board
    if B < N + M - 1:
        return "impossible"

    moves = []
    for i in range(1, N):
        moves.append(f'^ {i}')

    for j in range(1, M):
        moves.append(f'< {j}')
    
    return "possible\n" + "\n".join(moves)

# Reading input values
N, M, B = map(int, input().split())
blocks = [tuple(map(int, input().split())) for _ in range(B)]

# Calling the function and printing the output
print(solve_sliding_blocks(N, M, B, blocks))
```
