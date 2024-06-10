
def main():
    n_nodes = int(input())
    l = int(input())
    walk = [int(i) for i in input().split()]
    adj_list = {}
    for _ in range(n_nodes):
        neighbours = [int(i) for i in input().split()]
        adj_list[neighbours[0]] = neighbours[1:]

    print(main_func(n_nodes, l, walk, adj_list))


def main_func(n_nodes, l, walk, adj_list):
    paths = [[0] * n_nodes for _ in range(n_nodes)]
    for i in range(n_nodes):
        paths[i][i] = 1
    for k in range(n_nodes):
        for i in range(n_nodes):
            for j in range(n_nodes):
                paths[i][j] += paths[i][k] * paths[k][j]
    chance = 1
    current_node = walk[0]
    for next_node in walk[1:]:
        chance *= paths[current_node][next_node] / (len(adj_list[current_node]) + 1)
        current_node = next_node
    return chance


main()

