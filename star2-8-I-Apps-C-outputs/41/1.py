
import sys
robot_width, robot_height = map(int, input().split())
robot_image = []
for _ in range(robot_height):
    robot_image.append(list(map(int, input().split())))
floor_width, floor_height = map(int, input().split())
floor_image = []
for _ in range(floor_height):
    floor_image.append(list(map(int, input().split())))
matches = []
for i in range(floor_height - robot_height + 1):
    for j in range(floor_width - robot_width + 1):
        count = 0
        for k in range(robot_height):
            for l in range(robot_width):
                if robot_image[k][l] == floor_image[i + k][j + l]:
                    count += 1
        matches.append((count, i, j))
matches = sorted(matches, key=lambda x: (-x[0], x[1], x[2]))
for match in matches:
    print(match[2], match[1])

