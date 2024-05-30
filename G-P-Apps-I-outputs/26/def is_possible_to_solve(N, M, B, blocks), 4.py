
def is_possible_to_solve(N, M, B, blocks):
    visited = set()
    for r, c in blocks:
        visited.add((r, c))

    moves = []
    current_row, current_col = blocks[0]

    for target_row, target_col in blocks[1:]:
        while current_row < target_row:
            moves.append(('v', current_row + 1))
            current_row += 1
        while current_row > target_row:
            moves.append(('^', current_row))
            current_row -= 1
        while current_col < target_col:
            moves.append(('>', current_col + 1))
            current_col += 1
        while current_col > target_col:
            moves.append(('<', current_col))
            current_col -= 1

    return moves

# Input parsing
N, M, B = map(int, input().split())
blocks = [tuple(map(int, input().split())) for _ in range(B)]

moves = is_possible_to_solve(N, M, B, blocks)

if len(moves) == B - 1:
    print("possible")
    for move in moves:
        print(move[0], move[1])
else:
    print("impossible")
```
