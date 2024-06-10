
import sys
input = sys.stdin.readline

def main():
    N, X, Y = map(int, input().split())
    graph = [[] for _ in range(N)]
    for i in range(N-1):
        graph[i].append(i+1)
        graph[i+1].append(i)
    graph[X-1].append(Y-1)
    graph[Y-1].append(X-1)
    dist = [[-1] * N for _ in range(N)]
    for i in range(N):
        q = [i]
        dist[i][i] = 0
        while q:
            v = q.pop()
            for u in graph[v]:
                if dist[i][u] == -1:
                    dist[i][u] = dist[i][v] + 1
                    q.append(u)
    for k in range(1, N):
        cnt = 0
        for i in range(N):
            for j in range(i+1, N):
                if dist[i][j] == k:
                    cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()

