
def is_inside(x1, y1, x2, y2, x3, y3, x4, y4, x, y):
    def orientation(x1, y1, x2, y2, x3, y3):
        val = (y2 - y1) * (x3 - x2) - (x2 - x1) * (y3 - y2)
        if val == 0:
            return 0
        return 1 if val > 0 else -1

    def is_on_segment(x1, y1, x2, y2, x, y):
        if x <= max(x1, x2) and x >= min(x1, x2) and y <= max(y1, y2) and y >= min(y1, y2):
            return True
        return False

    o1 = orientation(x1, y1, x2, y2, x, y)
    o2 = orientation(x2, y2, x3, y3, x, y)
    o3 = orientation(x3, y3, x4, y4, x, y)
    o4 = orientation(x4, y4, x1, y1, x, y)

    if o1 == o2 == o3 == o4 == 1 or o1 == o2 == o3 == o4 == -1:
        return True

    if o1 == 0 and is_on_segment(x1, y1, x2, y2, x, y):
        return True
    if o2 == 0 and is_on_segment(x2, y2, x3, y3, x, y):
        return True
    if o3 == 0 and is_on_segment(x3, y3, x4, y4, x, y):
        return True
    if o4 == 0 and is_on_segment(x4, y4, x1, y1, x, y):
        return True

    return False

def count_dangerous_castles(N, nazis, S, castles):
    count = 0
    for castle in castles:
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    for l in range(k+1, N):
                        if is_inside(nazis[i][0], nazis[i][1], nazis[j][0], nazis[j][1], nazis[k][0], nazis[k][1], nazis[l][0], nazis[l][1], castle[0], castle[1]):
                            count += 1
                            break
    return count

# Input processing
N = int(input())
nazis = []
for _ in range(N):
    x, y = map(int, input().split())
    nazis.append((x, y))

S = int(input())
castles = []
for _ in range(S):
    x, y = map(int, input().split())
    castles.append((x, y))

# Count dangerous castles
result = count_dangerous_castles(N, nazis, S, castles)
print(result)
