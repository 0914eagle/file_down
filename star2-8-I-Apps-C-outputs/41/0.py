
import sys

robot_width, robot_height = map(int, input().split())
robot_image = [list(map(int, input().split())) for _ in range(robot_height)]
floor_width, floor_height = map(int, input().split())
floor_image = [list(map(int, input().split())) for _ in range(floor_height)]

best_match_count = 0
best_matches = []
for x in range(floor_width - robot_width + 1):
    for y in range(floor_height - robot_height + 1):
        match_count = 0
        for dx in range(robot_width):
            for dy in range(robot_height):
                if robot_image[dy][dx] == floor_image[y + dy][x + dx]:
                    match_count += 1
        if match_count > best_match_count:
            best_match_count = match_count
            best_matches = [(x, y)]
        elif match_count == best_match_count:
            best_matches.append((x, y))

for x, y in best_matches:
    print(x, y)

