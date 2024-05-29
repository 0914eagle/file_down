
def min_vertical_moves(n, m, malls):
    vertical_moves = 0
    item_to_mall = {i: [] for i in range(1, m+1)}
    
    for mall in malls:
        x, y, t = mall
        item_to_mall[t].append((x, y))
    
    for item, malls_list in item_to_mall.items():
        malls_list.sort(key=lambda mall: abs(mall[0]) - abs(mall[1]))
        shortest_path_y = sum(1 for x, y in malls_list if y < 0)
        shortest_path_x = len(malls_list) - shortest_path_y

        vertical_moves += min(shortest_path_x, shortest_path_y)

    return vertical_moves

n, m = map(int, input().split())
malls = [list(map(int, input().split())) for _ in range(n)]

result = min_vertical_moves(n, m, malls)
print(result)
```
