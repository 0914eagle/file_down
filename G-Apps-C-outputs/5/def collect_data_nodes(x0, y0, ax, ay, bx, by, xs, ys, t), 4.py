
def collect_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t):
    nodes = [(x0, y0)]
    while True:
        x_next = ax * nodes[-1][0] + bx
        y_next = ay * nodes[-1][1] + by
        if x_next > 10**16 or y_next > 10**16:
            break
        nodes.append((x_next, y_next))
    
    nodes_collected = 0
    for node in nodes:
        time_spent = abs(xs - node[0]) + abs(ys - node[1])  # time taken to reach the node
        if t - time_spent >= 0:  # check if there is enough time to collect the node
            nodes_collected += 1
            t -= time_spent
    
    return nodes_collected

# Input parsing
x0, y0, ax, ay, bx, by = map(int, input().split())
xs, ys, t = map(int, input().split())

result = collect_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t)
print(result)
