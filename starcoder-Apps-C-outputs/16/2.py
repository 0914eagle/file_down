
# , 2018

def main():
    # input
    n, m = map(int, input().split())
    IOUs = []
    for _ in range(m):
        IOUs.append(list(map(int, input().split())))

    # create adjacency matrix
    adj = [[0 for _ in range(n)] for _ in range(n)]
    for i in IOUs:
        adj[i[0]][i[1]] = i[2]

    # floyd warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adj[i][k] > 0 and adj[k][j] > 0:
                    adj[i][j] = max(adj[i][j], min(adj[i][k], adj[k][j]))
    output = []
    for i in range(n):
        for j in range(n):
            if adj[i][j] > 0:
                output.append([i, j, adj[i][j]])
    print(len(output))
    for o in output:
        print(o[0], o[1], o[2])

if __name__ == '__main__':
    main()
