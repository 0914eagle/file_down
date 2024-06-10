
import sys

robot_img = []
floor_img = []

robot_w, robot_h = map(int, input().split())
for _ in range(robot_h):
  robot_img.append(list(map(int, input().split())))
floor_w, floor_h = map(int, input().split())
for _ in range(floor_h):
  floor_img.append(list(map(int, input().split())))

robot_pixel_count = 0
for i in range(robot_h):
  for j in range(robot_w):
    if robot_img[i][j] == 1:
      robot_pixel_count += 1

max_same_pixel_count = 0
candidates = []
for i in range(floor_h - robot_h + 1):
  for j in range(floor_w - robot_w + 1):
    same_pixel_count = 0
    for k in range(robot_h):
      for l in range(robot_w):
        if robot_img[k][l] == floor_img[i+k][j+l]:
          same_pixel_count += 1
    if same_pixel_count == robot_pixel_count:
      max_same_pixel_count = same_pixel_count
      candidates.append((j, i))

candidates.sort(key=lambda x: (x[0], x[1]))
for x, y in candidates:
  print(x, y)

