
from sys import stdin

def main():
robot_width, robot_height = map(int, stdin.readline().split())
robot_image = [stdin.readline().split() for _ in range(robot_height)]
floor_width, floor_height = map(int, stdin.readline().split())
floor_image = [stdin.readline().split() for _ in range(floor_height)]
max_matches = 0
candidates = []
for y in range(floor_height - robot_height + 1):
for x in range(floor_width - robot_width + 1):
matches = 0
for robot_y in range(robot_height):
for robot_x in range(robot_width):
if robot_image[robot_y][robot_x] == floor_image[y + robot_y][x + robot_x]:
matches += 1
if matches >= max_matches:
if matches > max_matches:
candidates = []
max_matches = matches
candidates.append((x, y))
for x, y in candidates:
print(x, y)


if __name__ == "__main__":
main()

