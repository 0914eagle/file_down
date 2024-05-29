
def solve_sliding_blocks():
    # Read input
    N, M, B = map(int, input().split())
    target_board = set()
    for _ in range(B):
        r, c = map(int, input().split())
        target_board.add((r, c))

    # Check if it is possible to solve
    current_block = [(1, 1)]
    for _ in range(B-1):
        next_block = (0, 0)
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_r, new_c = current_block[-1][0] + dr, current_block[-1][1] + dc
            if 1 <= new_r <= N and 1 <= new_c <= M and (new_r, new_c) not in target_board:
                next_block = (new_r, new_c)
                break
        
        if next_block == (0, 0):
            print("impossible")
            return
        current_block.append(next_block)

    # Output the moves
    print("possible")
    for block in current_block[1:]:
        if block[0] == current_block[-1][0]:
            if block[1] > current_block[-1][1]:
                print("> " + str(block[0]))
            else:
                print("< " + str(block[0]))
        else:
            if block[0] > current_block[-1][0]:
                print("v " + str(block[1]))
            else:
                print("^ " + str(block[1]))

# Call the function to solve the sliding blocks problem
solve_sliding_blocks()
```
