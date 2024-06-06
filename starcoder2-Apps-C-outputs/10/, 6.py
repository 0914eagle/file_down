
from sys import stdin

n = int(stdin.readline())

dist = [[0 for i in range(n)] for j in range(n)]

for i in range(n-1):
    dist[i][i] = 0
    line = stdin.readline().split()
    for j in range(i+1, n):
        dist[i][j] = int(line[j-i-1])
        dist[j][i] = dist[i][j]

def min_disparity(dist, n):
    if n == 1:
        return 0
    if n == 2:
        return dist[0][1]
    if n == 3:
        return min(dist[0][1], dist[0][2], dist[1][2])

    min_dis = 10**10
    for i in range(1, n-1):
        min_dis = min(min_dis, dist[0][i] + min_disparity(dist[i:], n-i))
    return min_dis

print(min_disparity(dist, n))
