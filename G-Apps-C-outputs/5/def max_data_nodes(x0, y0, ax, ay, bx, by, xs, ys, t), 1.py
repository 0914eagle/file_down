
def max_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t):
    data_nodes = [(x0, y0)]
    for i in range(1, 5):
        x_new = ax * data_nodes[i-1][0] + bx
        y_new = ay * data_nodes[i-1][1] + by
        data_nodes.append((x_new, y_new))

    time_taken = lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2)

    max_nodes = 0
    for i in range(5):
        time_remaining = t
        nodes_collected = 0
        current_pos = (xs, ys)
        for j in range(i, 5):
            data_node = data_nodes[j]
            time_to_node = time_taken(current_pos[0], current_pos[1], data_node[0], data_node[1])
            if time_to_node <= time_remaining:
                time_remaining -= time_to_node
                time_remaining -= 1  # Collecting the node
                nodes_collected += 1
                current_pos = data_node
            else:
                break
        max_nodes = max(max_nodes, nodes_collected)

    return max_nodes

# Input parsing
x0, y0, ax, ay, bx, by = map(int, input().split())
xs, ys, t = map(int, input().split())

result = max_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t)
print(result)
