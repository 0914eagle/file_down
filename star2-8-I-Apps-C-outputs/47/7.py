
n, m = map(int, input().split())
plants = []
for _ in range(n):
    s, x = map(float, input().split())
    plants.append((s, x))
def is_valid(plants, border, m):
    curr_species = 1
    for _, x in plants:
        if x < border[curr_species]:
            curr_species += 1
            if curr_species > m:
                return False
    return True
left, right = 0, 10**9
while right - left > 1:
    mid = (left + right) // 2
    border = [0]
    for s, x in plants:
        if s != 1:
            continue
        if x > mid:
            break
        border.append(x)
    if len(border) < m:
        left = mid
    else:
        right = mid
border = [0]
for s, x in plants:
    if s != 1:
        continue
    if x > left:
        break
    border.append(x)
if is_valid(plants, border, m):
    print(0)
else:
    count = 0
    for s, x in plants:
        if x < left[s]:
            count += 1
    print(count)

