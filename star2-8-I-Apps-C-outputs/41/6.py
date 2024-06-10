
def get_max_matches(robot, floor):
    max_matches = 0
    for i in range(len(floor) - len(robot) + 1):
        for j in range(len(floor[0]) - len(robot[0]) + 1):
            matches = 0
            for x in range(len(robot)):
                for y in range(len(robot[0])):
                    if robot[x][y] == floor[i + x][j + y]:
                        matches += 1
            if matches > max_matches:
                max_matches = matches
    return max_matches

robot_width, robot_height = map(int, input().split())
robot = []
for _ in range(robot_height):
    robot.append(list(map(int, input().split())))
floor_width, floor_height = map(int, input().split())
floor = []
for _ in range(floor_height):
    floor.append(list(map(int, input().split())))
max_matches = get_max_matches(robot, floor)
candidates = []
for i in range(len(floor) - len(robot) + 1):
    for j in range(len(floor[0]) - len(robot[0]) + 1):
        matches = 0
        for x in range(len(robot)):
            for y in range(len(robot[0])):
                if robot[x][y] == floor[i + x][j + y]:
                    matches += 1
        if matches == max_matches:
            candidates.append((i, j))

for candidate in candidates:
    print(*candidate)

