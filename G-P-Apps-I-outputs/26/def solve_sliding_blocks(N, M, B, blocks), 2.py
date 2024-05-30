
def solve_sliding_blocks(N, M, B, blocks):
    initial_block = blocks[0]
    target_blocks = blocks[1:]
    
    if len(target_blocks) == 0:
        return "possible"
    
    if len(target_blocks) == 1:
        r, c = target_blocks[0]
        if r == N and c == M:
            return "possible\n< {}\n^ {}".format(N, M)
        elif r == 1 and c == 1:
            return "possible\n> 1\nv 1"
        elif r == N and c == 1:
            return "possible\n< {}\n^ {}".format(N, 1)
        elif r == 1 and c == M:
            return "possible\n> 1\n^ {}".format(M)
        else:
            return "impossible"
    
    target_rows = set([r for r, c in target_blocks])
    target_cols = set([c for r, c in target_blocks])
    
    if len(target_rows) == 1:
        r = target_rows.pop()
        moves = "< {}\n" * (r-1) + "^ {}\n" * (M-1)
        return "possible\n" + moves.format(r)
    
    if len(target_cols) == 1:
        c = target_cols.pop()
        moves = "^ {}\n" * (c-1) + "< {}\n" * (N-1)
        return "possible\n" + moves.format(c)
    
    return "impossible"

# Read input
N, M, B = map(int, input().split())
blocks = [tuple(map(int, input().split())) for _ in range(B)]

# Solve the problem
result = solve_sliding_blocks(N, M, B, blocks)
print(result)
```
