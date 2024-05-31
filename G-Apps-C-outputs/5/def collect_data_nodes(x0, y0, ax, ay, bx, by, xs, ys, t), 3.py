
def collect_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t):
    nodes = [(x0, y0)]
    while len(nodes) <= t + 1:
        xi = ax * nodes[-1][0] + bx
        yi = ay * nodes[-1][1] + by
        nodes.append((xi, yi))

    collected = 0
    max_nodes = 0
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            distance = abs(nodes[i][0] - xs) + abs(nodes[i][1] - ys) + abs(nodes[j][0] - nodes[i][0]) + abs(nodes[j][1] - nodes[i][1])
            if distance <= t:
                max_nodes = max(max_nodes, j - i)
    return max_nodes

# Input parsing
x0, y0, ax, ay, bx, by = map(int, input().split())
xs, ys, t = map(int, input().split())

# Call the function and output the result
result = collect_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t)
print(result)
