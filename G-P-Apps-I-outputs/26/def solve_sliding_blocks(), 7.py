
def solve_sliding_blocks():
    # Read input
    N, M, B = map(int, input().split())
    target_blocks = [tuple(map(int, input().split())) for _ in range(B)]

    # Check if the target configuration is reachable
    reachable = True
    for i in range(1, B):
        r_diff = abs(target_blocks[i][0] - target_blocks[i-1][0])
        c_diff = abs(target_blocks[i][1] - target_blocks[i-1][1])
        if r_diff > 1 or c_diff > 1 or (r_diff == 0 and c_diff == 0):
            reachable = False

    if not reachable:
        print("impossible")
    else:
        print("possible")
        # Generate moves to reach the target configuration
        moves = []
        for i in range(1, B):
            r_diff = target_blocks[i][0] - target_blocks[i-1][0]
            c_diff = target_blocks[i][1] - target_blocks[i-1][1]
            if r_diff == 1:
                moves.append(f"v {target_blocks[i][1]}")
            elif r_diff == -1:
                moves.append(f"^ {target_blocks[i][1]}")
            elif c_diff == 1:
                moves.append(f"> {target_blocks[i][0]}")
            elif c_diff == -1:
                moves.append(f"< {target_blocks[i][0]}")

        for move in moves:
            print(move)

# Call the function to solve the sliding blocks problem
solve_sliding_blocks()
```
