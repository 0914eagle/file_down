
def solve_sliding_blocks(N, M, B, blocks):
    def is_connected(block1, block2):
        r1, c1 = block1
        r2, c2 = block2
        return (abs(r1 - r2) + abs(c1 - c2)) == 1

    blocks = [(r - 1, c - 1) for r, c in blocks]

    if B == 1:
        print("possible")
        return

    visited = set()
    moves = []
    for i in range(1, B):
        found = False
        for j in range(i, B):
            if is_connected(blocks[i - 1], blocks[j]) and blocks[j] not in visited:
                visited.add(blocks[j])
                blocks[i], blocks[j] = blocks[j], blocks[i]
                found = True
                if blocks[i] != blocks[i - 1]:
                    if blocks[i][1] < blocks[i - 1][1]:
                        moves.append(f"< {blocks[i][0] + 1}")
                    elif blocks[i][1] > blocks[i - 1][1]:
                        moves.append(f"> {blocks[i][0] + 1}")
                    elif blocks[i][0] < blocks[i - 1][0]:
                        moves.append(f"^ {blocks[i][1] + 1}")
                    else:
                        moves.append(f"v {blocks[i][1] + 1}")
                break
        if not found:
            print("impossible")
            return

    print("possible")
    for move in moves:
        print(move)

# Read input
N, M, B = map(int, input().split())
blocks = [tuple(map(int, input().split())) for _ in range(B)]

# Call the function
solve_sliding_blocks(N, M, B, blocks)
```
