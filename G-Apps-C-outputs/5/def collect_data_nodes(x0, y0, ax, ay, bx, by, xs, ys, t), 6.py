
def collect_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t):
    def calculate_distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def calculate_coordinates(i):
        if i == 0:
            return x0, y0
        prev_x, prev_y = calculate_coordinates(i - 1)
        new_x = ax * prev_x + bx
        new_y = ay * prev_y + by
        return new_x, new_y

    data_nodes = []
    max_nodes = 0

    for i in range(100):  # Adjust the range if necessary
        x, y = calculate_coordinates(i)
        if x > 10**16 or y > 10**16:
            break
        data_nodes.append((x, y))

    for i in range(len(data_nodes)):
        total_time = 0
        collected_nodes = 0
        for j in range(i, len(data_nodes)):
            x, y = data_nodes[j]
            time_to_node = calculate_distance(xs, ys, x, y)
            if total_time + time_to_node <= t:
                total_time += time_to_node
                total_time += 1  # Time to collect the node
                collected_nodes += 1
            else:
                break
        max_nodes = max(max_nodes, collected_nodes)

    return max_nodes

# Input parsing
x0, y0, ax, ay, bx, by = map(int, input().split())
xs, ys, t = map(int, input().split())

result = collect_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t)
print(result)
