
# -*- coding: utf-8 -*-


def main():
    N = int(input())
    direction = input()
    grid = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'R':
                x, y = i, j
    idx = 0
    path = [[x, y]]
    #check
    flag = 0
    for i in range(N):
        if grid[i][0] != '#' or grid[i][N-1] != '#':
            flag = 1
            break
    for i in range(N):
        if grid[0][i] != '#' or grid[N-1][i] != '#':
            flag = 1
            break
    if flag == 1:
        print(1)
        return
    while True:
        if direction[idx] == '>':
            y += 1
        elif direction[idx] == '<':
            y -= 1
        elif direction[idx] == '^':
            x -= 1
        elif direction[idx] == 'v':
            x += 1
        if 0 <= x < N and 0 <= y < N and grid[x][y] != '#':
            path.append([x, y])
        else:
            idx += 1
            if idx == len(direction):
                idx = 0
        if len(path) > 1:
            if path[-1] == path[0]:
                print(len(path)-1)
                return
        if [x, y] in path[:-1]:
            print(len(path)-path[:-1].index([x, y]))
            return

if __name__ == '__main__':
    main()
