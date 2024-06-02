
def is_inside(x1, y1, x2, y2, x3, y3, x4, y4, x, y):
    def cross_product(x1, y1, x2, y2):
        return x1 * y2 - x2 * y1

    def is_on_segment(x1, y1, x2, y2, x, y):
        return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)

    def orientation(x1, y1, x2, y2, x3, y3):
        val = (y2 - y1) * (x3 - x2) - (x2 - x1) * (y3 - y2)
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    o1 = orientation(x1, y1, x2, y2, x, y)
    o2 = orientation(x2, y2, x3, y3, x, y)
    o3 = orientation(x3, y3, x4, y4, x, y)
    o4 = orientation(x4, y4, x1, y1, x, y)

    if o1 == o2 == o3 == o4:
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

def count_dangerous_castles(N, nazi_troops, S, soviet_castles):
    count = 0
    for castle in soviet_castles:
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    for l in range(k+1, N):
                        if is_inside(nazi_troops[i][0], nazi_troops[i][1], nazi_troops[j][0], nazi_troops[j][1],
                                     nazi_troops[k][0], nazi_troops[k][1], nazi_troops[l][0], nazi_troops[l][1],
                                     castle[0], castle[1]):
                            count += 1
                            break
    return count

# Input processing
N = int(input())
nazi_troops = [list(map(int, input().split())) for _ in range(N)]
S = int(input())
soviet_castles = [list(map(int, input().split())) for _ in range(S)]

# Count dangerous castles
result = count_dangerous_castles(N, nazi_troops, S, soviet_castles)
print(result)
