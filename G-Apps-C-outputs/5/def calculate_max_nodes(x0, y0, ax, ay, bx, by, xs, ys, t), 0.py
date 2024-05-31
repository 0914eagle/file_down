
def calculate_max_nodes(x0, y0, ax, ay, bx, by, xs, ys, t):
    nodes = [(x0, y0)]
    for i in range(1, 5):
        x_prev, y_prev = nodes[-1]
        x_new = ax * x_prev + bx
        y_new = ay * y_prev + by
        nodes.append((x_new, y_new))

    max_nodes = 0
    for i in range(5):
        dist_to_node = abs(xs - nodes[i][0]) + abs(ys - nodes[i][1])
        time_left = t - dist_to_node
        if time_left < 0:
            continue
        num_nodes = min(i + 1, time_left // 2)
        max_nodes = max(max_nodes, num_nodes)

    return max_nodes

# Input parsing
x0, y0, ax, ay, bx, by = map(int, input().split())
xs, ys, t = map(int, input().split())

print(calculate_max_nodes(x0, y0, ax, ay, bx, by, xs, ys, t))
