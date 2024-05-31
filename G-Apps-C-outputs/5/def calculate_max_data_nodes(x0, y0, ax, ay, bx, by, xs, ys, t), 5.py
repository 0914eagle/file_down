
def calculate_max_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t):
    nodes = [(x0, y0)]
    for i in range(1, 5):
        xi = ax * nodes[i-1][0] + bx
        yi = ay * nodes[i-1][1] + by
        nodes.append((xi, yi))

    data_nodes = set(nodes)

    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def can_reach_in_time(p1, p2, time_left):
        return time_left >= manhattan_distance(p1, p2)

    def find_closest_node(current_pos, time_left):
        closest_node = None
        min_distance = float('inf')
        for node in data_nodes:
            distance = manhattan_distance(current_pos, node)
            if distance < min_distance and can_reach_in_time(current_pos, node, time_left - distance):
                min_distance = distance
                closest_node = node
        return closest_node, min_distance

    current_pos = (xs, ys)
    time_left = t
    collected_nodes = 0
    while time_left > 0:
        next_node, distance = find_closest_node(current_pos, time_left)
        if next_node is not None:
            data_nodes.remove(next_node)
            collected_nodes += 1
            time_left -= distance
            current_pos = next_node
        else:
            break

    return collected_nodes

# Input parsing
x0, y0, ax, ay, bx, by = map(int, input().split())
xs, ys, t = map(int, input().split())

result = calculate_max_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t)
print(result)
