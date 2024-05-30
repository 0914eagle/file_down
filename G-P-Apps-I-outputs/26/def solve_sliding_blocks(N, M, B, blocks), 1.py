
def solve_sliding_blocks(N, M, B, blocks):
    if B == 1:
        return "impossible"
    
    board = [[0 for _ in range(M)] for _ in range(N)]
    for r, c in blocks:
        board[r - 1][c - 1] = 1

    moves = []
    for i in range(1, B):
        r1, c1 = blocks[i - 1]
        r2, c2 = blocks[i]

        while r1 < r2:
            moves.append(f"v {r1}")
            r1 += 1
        while r1 > r2:
            moves.append(f"^ {r1}")
            r1 -= 1
        while c1 < c2:
            moves.append(f"> {c1}")
            c1 += 1
        while c1 > c2:
            moves.append(f"< {c1}")
            c1 -= 1

    return "possible\n" + "\n".join(moves)

# Example Input Parsing
input_str = "3 4 6\n1 1\n1 2\n2 2\n2 3\n3 3\n3 4"
input_lines = input_str.strip().split("\n")
N, M, B = map(int, input_lines[0].split())
blocks = [tuple(map(int, line.split())) for line in input_lines[1:]]

# Solve the problem
output_str = solve_sliding_blocks(N, M, B, blocks)
print(output_str)
```
