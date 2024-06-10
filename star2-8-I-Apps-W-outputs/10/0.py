
n = int(input())
angles = list(map(int, input().split()))
angles.sort()
min_diff = 360
for i in range(n):
    first_sector = angles[:i + 1]
    second_sector = angles[i + 1:]
    diff = abs(sum(first_sector) - sum(second_sector))
    min_diff = min(min_diff, diff)
print(min_diff)

