
# 1. 先把初始的状态和目标状态存起来
# 2. 然后从初始状态开始遍历，如果当前状态和目标状态相同，则返回1
# 3. 如果当前状态和目标状态不相同，则遍历当前状态的每一个状态，如果当前状态的状态和目标状态相同，则返回1
# 4. 如果当前状态的状态和目标状态不相同，则返回0

import sys
sys.setrecursionlimit(1000000)

def dfs(i, j, state):
    if i == r and j == c:
        if state == target:
            return 1
        else:
            return 0
    if state[i][j] == target[i][j]:
        if dfs(i+1, j, state):
            return 1
        if dfs(i, j+1, state):
            return 1
    else:
        if state[i][j] == 'O':
            state[i][j] = 'X'
            for k in range(c):
                if state[i][k] == 'O':
                    state[i][k] = 'X'
                else:
                    state[i][k] = 'O'
            for k in range(r):
                if state[k][j] == 'O':
                    state[k][j] = 'X'
                else:
                    state[k][j] = 'O'
            if dfs(i+1, j, state):
                return 1
            if dfs(i, j+1, state):
                return 1
        else:
            if dfs(i+1, j, state):
                return 1
            if dfs(i, j+1, state):
                return 1
    return 0

r, c = map(int, input().split())
state = []
target = []
for i in range(r):
    state.append(list(input()))
for i in range(r):
    target.append(list(input()))

print(dfs(0, 0, state))
