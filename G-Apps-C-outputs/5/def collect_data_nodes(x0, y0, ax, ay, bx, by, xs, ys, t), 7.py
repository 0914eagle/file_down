
def collect_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t):
    data_nodes = [(x0, y0)]
    while True:
        new_x = ax * data_nodes[-1][0] + bx
        new_y = ay * data_nodes[-1][1] + by
        if new_x < 1 or new_y < 1:
            break
        data_nodes.append((new_x, new_y))
    
    max_nodes = 0
    for node in data_nodes:
        dist = abs(xs - node[0]) + abs(ys - node[1])
        if dist <= t:
            t -= dist
            max_nodes += 1
        else:
            break
    
    return max_nodes

# Input processing
x0, y0, ax, ay, bx, by = map(int, input().split())
xs, ys, t = map(int, input().split())

# Call the function and print the result
print(collect_data_nodes(x0, y0, ax, ay, bx, by, xs, ys, t))
