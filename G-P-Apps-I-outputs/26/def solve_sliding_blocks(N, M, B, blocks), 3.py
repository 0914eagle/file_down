
def solve_sliding_blocks(N, M, B, blocks):
    def find_path(start, visited):
        if start in visited:
            return False
        visited.add(start)
        for i in range(N):
            for j in range(M):
                if (i, j) in blocks and abs(i-start[0]) + abs(j-start[1]) == 1:
                    if find_path((i, j), visited):
                        return True
        return False

    if not find_path(blocks[0], set()):
        print("impossible")
        return

    moves = []
    for i in range(1, B):
        target_row, target_col = blocks[i]
        while target_row > i:
            moves.append(f"v {target_row}")
            target_row -= 1
        while target_row < i:
            moves.append(f"^ {target_row+1}")
            target_row += 1
        while target_col > 1:
            moves.append(f"< {target_col}")
            target_col -= 1
            moves.append(f"> {target_col}")
        moves.append(f"< 1")

    print("possible")
    for move in moves:
        print(move)

# Input
N, M, B = map(int, input().split())
blocks = [tuple(map(int, input().split())) for _ in range(B)]

# Solve
solve_sliding_blocks(N, M, B, blocks)
```
