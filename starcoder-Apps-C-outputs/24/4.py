
# python 3.6
# author : hitchhiker42
# time : 06/Oct/2018
# problem : https://codeforces.com/problemset/problem/893/C
# editor : vscode

def main():
    n = int(input())
    cells = [list(input()) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and cells[i][j] == 'E':
                mark = True
                for k in range(n):
                    if cells[i][k] == 'E' or cells[k][j] == 'E':
                        mark = False
                        break
                if mark == False:
                    return -1
                else:
                    for k in range(n):
                        visited[i][k] = True
                        visited[k][j] = True
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                visited[i][j] = True
                count += 1
    return count

print(main())

