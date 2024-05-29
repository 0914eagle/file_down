
def minimum_vertical_moves(n, m, malls):
    items_dict = {i: [] for i in range(1, m+1)}
    
    for x, y, item in malls:
        items_dict[item].append((x, y))
    
    vertical_moves_count = 0
    
    for item in items_dict.values():
        min_y = min(y for x, y in item)
        max_y = max(y for x, y in item)
        
        if any(abs(x) < max_y for x, _ in item) and any(abs(x) > min_y for x, _ in item):
            vertical_moves_count += 1
    
    return vertical_moves_count

# Input parsing
n, m = map(int, input().split())
malls = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(minimum_vertical_moves(n, m, malls))
