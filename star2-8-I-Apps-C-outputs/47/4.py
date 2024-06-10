
n, m = map(int, input().split())
plants = [list(map(float, input().split())) for i in range(n)]

count = 0
for i in range(n):
    if plants[i][0] != i + 1:
        count += 1
print(count)

