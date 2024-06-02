
def is_inside(x1, y1, x2, y2, x3, y3, x4, y4, x, y):
    def cross_product(x1, y1, x2, y2):
        return x1 * y2 - x2 * y1

    def is_on_segment(x1, y1, x2, y2, x, y):
        return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)

    def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
        d1 = cross_product(x4 - x3, y4 - y3, x1 - x3, y1 - y3)
        d2 = cross_product(x4 - x3, y4 - y3, x2 - x3, y2 - y3)
        d3 = cross_product(x2 - x1, y2 - y1, x3 - x1, y3 - y1)
        d4 = cross_product(x2 - x1, y2 - y1, x4 - x1, y4 - y1)
        return (d1 * d2 < 0) and (d3 * d4 < 0)

    count = 0
    for i in range(4):
        x1, y1, x2, y2, x3, y3, x4, y4 = x2, y2, x3, y3, x4, y4, x1, y1
        if is_on_segment(x1, y1, x2, y2, x, y):
            count += 1
        elif is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
            count += 1
    return count == 4

def count_dangerous_castles(N, nazis, S, castles):
    count = 0
    for castle in castles:
        x, y = castle
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    for l in range(k+1, N):
                        x1, y1 = nazis[i]
                        x2, y2 = nazis[j]
                        x3, y3 = nazis[k]
                        x4, y4 = nazis[l]
                        if is_inside(x1, y1, x2, y2, x3, y3, x4, y4, x, y):
                            count += 1
                            break
    return count

# Input
N = int(input())
nazis = [list(map(int, input().split())) for _ in range(N)]
S = int(input())
castles = [list(map(int, input().split())) for _ in range(S)]

# Output
print(count_dangerous_castles(N, nazis, S, castles))
