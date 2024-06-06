
'''
4 5
0 1 10
1 2 10
0 3 10
3 2 10
2 0 20
'''

from collections import defaultdict

n, m = map(int,input().split())

matrix = defaultdict(dict)

for i in range(m):
    a,b,c = map(int,input().split())

    if b in matrix[a]:
        matrix[a][b] += c
    else:
        matrix[a][b] = c


def find_shortest_path(matrix,start,end):
    stack = []
    visited = []
    stack.append(start)
    while stack:
        current = stack.pop()
        visited.append(current)
        if current == end:
            return visited
        else:
            for key,value in matrix[current].items():
                if key not in visited and key not in stack:
                    stack.append(key)
                    

while True:
    flag = False
    for i in range(n):
        for j in range(n):
            if i!=j and i in matrix and j in matrix:
                if j in matrix[i]:
                    flag = True
                    break
    if not flag:
        break
    else:
        path = find_shortest_path(matrix,i,j)
        min_val = 1000000
        for i in range(len(path)-1):
            if matrix[path[i]][path[i+1]] < min_val:
                min_val = matrix[path[i]][path[i+1]]
        for i in range(len(path)-1):
            matrix[path[i]][path[i+1]] -= min_val
            matrix[path[i+1]][path[i]] = min_val

count = 0
for i in matrix:
    for j in matrix[i]:
        if matrix[i][j] != 0:
            count += 1
print(count)
for i in matrix:
    for j in matrix[i]:
        if matrix[i][j] != 0:
            print(i,j,matrix[i][j])
