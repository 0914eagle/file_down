
def solve_sliding_blocks(N, M, B, blocks):
    initial_board = {(1, 1)}
    target_board = set(blocks)
    
    def can_reach_target(init, target):
        queue = [init]
        visited = set(init)
        
        while queue:
            curr_block = queue.pop(0)
            if curr_block in target:
                return True
            
            r, c = curr_block
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r + dr, c + dc
                if 1 <= new_r <= N and 1 <= new_c <= M and (new_r, new_c) not in visited:
                    queue.append((new_r, new_c))
                    visited.add((new_r, new_c))
        
        return False
    
    if not can_reach_target((1, 1), target_board):
        return "impossible"
    
    moves = []
    for block in blocks[1:]:
        row_diff = block[0] - 1
        col_diff = block[1] - 1
        
        if row_diff > 0:
            moves.append("^ " + str(block[0]))
        if col_diff < 0:
            moves.append("> " + str(abs(col_diff)))
        if col_diff > 0:
            moves.append("< " + str(col_diff))
    
    return "possible", moves

# Input parsing and function call
inputs = input().strip().split()
N, M, B = int(inputs[0]), int(inputs[1]), int(inputs[2])
blocks = [tuple(map(int, input().strip().split())) for _ in range(B)]

result = solve_sliding_blocks(N, M, B, blocks)
if result == "impossible":
    print("impossible")
else:
    print("possible")
    for move in result[1]:
        print(move)
```
