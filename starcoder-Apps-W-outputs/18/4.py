
import sys
sys.stdin = open("input.txt")

n = int(input())

rooms_1 = []
rooms_2 = []
for _ in range(n):
    rooms_1.append(list(map(int, input().split())))
for _ in range(n):
    rooms_2.append(list(map(int, input().split())))

possible = True
for i in range(n):
    for j in range(4):
        if rooms_1[i][j] != 0 and rooms_2[i][j] == 0:
            possible = False
            break
    if not possible:
        break
if possible:
    print("Yes")
else:
    print("No")
