
robot = [[int(x) for x in input().split()] for _ in range(int(input()))]
floor = [[int(x) for x in input().split()] for _ in range(int(input()))]
w, h = len(robot[0]), len(robot)
matches = []
for x in range(len(floor[0]) - w + 1):
    for y in range(len(floor) - h + 1):
        match = 0
        for i in range(w):
            for j in range(h):
                if floor[y+j][x+i] == robot[j][i]:
                    match += 1
        matches.append((match, x, y))
matches = sorted(matches)
for match, x, y in matches:
    if match == matches[-1][0]:
        print(x, y)

