
import sys
import os

def find_route(node):
    if len(edge_dict[node]) == 0:
        return
    next_node = edge_dict[node][0]
    if next_node == N:
        return
    else:
        find_route(next_node)


def solve():
    result = K
    for junction in range(1, K+1):
        find_route(junction)

    print(result)

def main():
    global N, K, M, edge_dict
    N, K, M = map(int, input().split())
    edge_dict = {}
    for i in range(1, N+1):
        edge_dict[i] = []
    for _ in range(M):
        a, b = map(int, input().split())
        edge_dict[a].append(b)

    solve()


if __name__ == '__main__':
    main()


