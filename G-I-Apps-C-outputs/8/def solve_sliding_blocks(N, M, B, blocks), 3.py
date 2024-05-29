
def solve_sliding_blocks(N, M, B, blocks):
    # Check if the target board is reachable
    def is_reachable(initial_block, target_block):
        r1, c1 = initial_block
        r2, c2 = target_block
        if r1 == r2 and c1 == c2:
            return True
        if r1 == r2:
            if c1 < c2:
                return all((r1, c) in blocks for c in range(c1, c2))
            else:
                return all((r1, c) in blocks for c in range(c2, c1))
        if c1 == c2:
            if r1 < r2:
                return all((r, c1) in blocks for r in range(r1, r2))
            else:
                return all((r, c1) in blocks for r in range(r2, r1))
        return False

    # Check if the target board is reachable from the initial board
    if not is_reachable(blocks[0], blocks[1]):
        return "impossible"

    # Determine the moves needed to reach the target board
    moves = []
    for i in range(1, B):
        r1, c1 = blocks[i - 1]
        r2, c2 = blocks[i]
        if r1 < r2:
            moves.append(f"v {r2}")
        elif r1 > r2:
            moves.append(f"^ {r2}")
        elif c1 < c2:
            moves.append(f"> {c2}")
        elif c1 > c2:
            moves.append(f"< {c2}")

    return "possible", moves

# Input parsing
N, M, B = map(int, input().split())
blocks = [tuple(map(int, input().split())) for _ in range(B)]

# Solve and output
result = solve_sliding_blocks(N, M, B, blocks)
if result == "impossible":
    print("impossible")
else:
    print("possible")
    for move in result[1]:
        print(move)
```
