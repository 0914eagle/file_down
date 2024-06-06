

# 分析：
# 本题的难点在于，在输入的两个地图中，数字相同的房间并不一定是同一间房间。
# 因此，我们需要记录下不同房间的连接情况。
# 可以使用字典表示，键是每个房间的编号，值是这个房间的出口情况，也就是出口1、出口2、出口3、出口4到达的房间。
# 然后就是DFS了。
# 注意，因为出口在不同房间中对应的房间是不同的，所以要用两个字典来记录。

import sys

N = int(sys.stdin.readline())
# 两个字典，分别记录两个地图中，每个房间的出口情况
origin, reverse = {}, {}

for i in range(1, N + 1):
    exits = sys.stdin.readline().split()
    origin[i] = exits

for i in range(1, N + 1):
    exits = sys.stdin.readline().split()
    reverse[i] = exits

def dfs(x, y):
    if x == y:
        return True
    # 注意此处一定要用origin字典，因为我们要的是两个地图中出口的对应关系
    exits = origin[x]
    for e in exits:
        if e == '0':
            continue
        elif dfs(int(e), y):
            return True
    return False

print('Yes' if dfs(1, N) else 'No')

