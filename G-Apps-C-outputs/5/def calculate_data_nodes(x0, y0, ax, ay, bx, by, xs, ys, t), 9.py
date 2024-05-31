
def calculate_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t):
    nodes = [(x0, y0)]
    for i in range(1, 5):
        x_i = ax * nodes[i-1][0] + bx
        y_i = ay * nodes[i-1][1] + by
        nodes.append((x_i, y_i))
    
    data_nodes = set(nodes)
    
    max_nodes = 0
    for i in range(len(nodes)):
        total_time = abs(xs - nodes[i][0]) + abs(ys - nodes[i][1])
        if total_time <= t:
            max_nodes = max(max_nodes, i + 1)
    
    return max_nodes

# Input parsing
x0, y0, ax, ay, bx, by = map(int, input().split())
xs, ys, t = map(int, input().split())

result = calculate_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t)
print(result)
