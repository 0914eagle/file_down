
def max_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t):
    nodes = [(x0, y0)]
    for i in range(1, 5):
        x = ax * nodes[i-1][0] + bx
        y = ay * nodes[i-1][1] + by
        nodes.append((x, y))

    data_nodes = set(nodes)
    current_pos = (xs, ys)
    collected_nodes = 0
    max_time = t

    for node in nodes:
        dist_x = abs(node[0] - current_pos[0])
        dist_y = abs(node[1] - current_pos[1])
        travel_time = dist_x + dist_y

        if travel_time <= max_time:
            max_time -= travel_time
            max_time += 1
            collected_nodes += 1
            current_pos = node

    return collected_nodes

# Input parsing
x0, y0, ax, ay, bx, by = map(int, input().split())
xs, ys, t = map(int, input().split())

result = max_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t)
print(result)
