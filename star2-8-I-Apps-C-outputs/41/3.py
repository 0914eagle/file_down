
def main():
W, H = map(int, input().split())
robot = []
for i in range(H):
robot.append(list(map(int, input().split())))
W, H = map(int, input().split())
floor = []
for i in range(H):
floor.append(list(map(int, input().split())))
matches = []
for i in range(H - len(robot) + 1):
for j in range(W - len(robot[0]) + 1):
same = 0
for k in range(len(robot)):
for l in range(len(robot[0])):
if robot[k][l] == floor[i + k][j + l]:
same += 1
if same == len(robot) * len(robot[0]):
matches.append((j, i))
for match in matches:
print(match[0], match[1])


if __name__ == '__main__':
main()

