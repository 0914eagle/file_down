
def is_inside(x1, y1, x2, y2, x3, y3, x4, y4, x, y):
    def cross_product(x1, y1, x2, y2):
        return x1 * y2 - x2 * y1

    def is_left(x1, y1, x2, y2, x, y):
        return cross_product(x2 - x1, y2 - y1, x - x1, y - y1) >= 0

    return is_left(x1, y1, x2, y2, x, y) and is_left(x2, y2, x3, y3, x, y) and is_left(x3, y3, x4, y4, x, y) and is_left(x4, y4, x1, y1, x, y)

def count_dangerous_castles(N, nazi_troops, S, soviet_castles):
    count = 0
    for i in range(S):
        x1, y1 = soviet_castles[i]
        for j in range(N):
            for k in range(j + 1, N):
                for l in range(k + 1, N):
                    for m in range(l + 1, N):
                        x2, y2 = nazi_troops[j]
                        x3, y3 = nazi_troops[k]
                        x4, y4 = nazi_troops[l]
                        x5, y5 = nazi_troops[m]
                        if is_inside(x2, y2, x3, y3, x4, y4, x5, y5, x1, y1):
                            count += 1
                            break
    return count

# Read input
N = int(input())
nazi_troops = [tuple(map(int, input().split())) for _ in range(N)]
S = int(input())
soviet_castles = [tuple(map(int, input().split())) for _ in range(S)]

# Calculate and output the number of castles in danger
print(count_dangerous_castles(N, nazi_troops, S, soviet_castles))
