
import sys
robot_w, robot_h = map(int, input().split())
robot_image = [list(map(int, input().split())) for _ in range(robot_h)]
floor_w, floor_h = map(int, input().split())
floor_image = [list(map(int, input().split())) for _ in range(floor_h)]

def match_image(robot_image, floor_image, x, y):
    robot_h = len(robot_image)
    robot_w = len(robot_image[0])
    floor_h = len(floor_image)
    floor_w = len(floor_image[0])
    if x + robot_w > floor_w or y + robot_h > floor_h:
        return -1
    match_count = 0
    for i in range(robot_h):
        for j in range(robot_w):
            if robot_image[i][j] == floor_image[y+i][x+j]:
                match_count += 1

    return match_count

max_match_count = 0
candidates = []
for y in range(floor_h - robot_h + 1):
    for x in range(floor_w - robot_w + 1):
        match_count = match_image(robot_image, floor_image, x, y)
        if match_count > max_match_count:
            max_match_count = match_count
            candidates = [(x, y)]
        elif match_count == max_match_count:
            candidates.append((x, y))

for x, y in candidates:
    print(x, y)

