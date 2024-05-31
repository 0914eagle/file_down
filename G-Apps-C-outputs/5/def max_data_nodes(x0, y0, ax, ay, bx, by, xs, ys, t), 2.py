
def max_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t):
    data_nodes = [(x0, y0)]
    while True:
        new_x = ax * data_nodes[-1][0] + bx
        new_y = ay * data_nodes[-1][1] + by
        if new_x <= 10**16 and new_y <= 10**16:
            data_nodes.append((new_x, new_y))
        else:
            break
    
    max_nodes = 0
    for i in range(len(data_nodes)):
        remaining_time = t
        collected_nodes = 0
        x, y = xs, ys
        for j in range(i, len(data_nodes)):
            dist_x = abs(data_nodes[j][0] - x)
            dist_y = abs(data_nodes[j][1] - y)
            total_dist = dist_x + dist_y
            if total_dist <= remaining_time:
                remaining_time -= total_dist
                collected_nodes += 1
                x, y = data_nodes[j][0], data_nodes[j][1]
            else:
                break
        max_nodes = max(max_nodes, collected_nodes)
    
    return max_nodes

# Input reading
x0, y0, ax, ay, bx, by = map(int, input().split())
xs, ys, t = map(int, input().split())

result = max_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t)
print(result)
