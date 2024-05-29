
def solve_sliding_blocks(N, M, B, blocks):
    initial_block = blocks[0]
    target_blocks = blocks[1:]

    # Check if the target blocks form a tree
    if not is_tree(target_blocks):
        print("impossible")
        return

    current_position = initial_block
    moves = []

    for target_block in target_blocks:
        move_row = None
        move_col = None

        # Determine the row move
        if target_block[0] > current_position[0]:
            move_row = 'v'
        elif target_block[0] < current_position[0]:
            move_row = '^'

        # Determine the column move
        if target_block[1] > current_position[1]:
            move_col = '>'
        elif target_block[1] < current_position[1]:
            move_col = '<'

        # Perform the row move first if applicable
        if move_row:
            moves.append(f"{move_row} {target_block[0]}")
            current_position = (target_block[0], current_position[1])

        # Perform the column move next if applicable
        if move_col:
            moves.append(f"{move_col} {target_block[1]}")
            current_position = (current_position[0], target_block[1])

    print("possible")
    for move in moves:
        print(move)

def is_tree(blocks):
    # Check if the blocks form a tree by checking for disjoint sets
    parent = {}
    for block in blocks:
        parent[block] = block

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            if (blocks[i][0] == blocks[j][0] and abs(blocks[i][1] - blocks[j][1]) == 1) or \
               (blocks[i][1] == blocks[j][1] and abs(blocks[i][0] - blocks[j][0]) == 1):
                union(blocks[i], blocks[j])

    root_set = set()
    for block in blocks:
        root_set.add(find(block))

    return len(root_set) == 1

# Read input
N, M, B = map(int, input().split())
blocks = []
blocks.append(tuple(map(int, input().split())))
for _ in range(B):
    blocks.append(tuple(map(int, input().split())))

# Call the function
solve_sliding_blocks(N, M, B, blocks)
```
