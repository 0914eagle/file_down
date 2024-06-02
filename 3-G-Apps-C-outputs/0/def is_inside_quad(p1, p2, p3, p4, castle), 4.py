
def is_inside_quad(p1, p2, p3, p4, castle):
    def cross_product(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    def is_same_side(p1, p2, p3, p4):
        cp1 = cross_product(p3, p4, p1)
        cp2 = cross_product(p3, p4, p2)
        return cp1 * cp2 >= 0

    return is_same_side(p1, p2, p3, p4) and is_same_side(p1, p3, p2, p4) and is_same_side(p1, p4, p2, p3)

def count_danger_castles(N, nazis, S, castles):
    danger_count = 0
    for i in range(S):
        for j in range(N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    if is_inside_quad(nazis[j], nazis[k], nazis[l], nazis[i], castles[i]):
                        danger_count += 1
                        break
    return danger_count

# Input
N = int(input())
nazis = [list(map(int, input().split())) for _ in range(N)]
S = int(input())
castles = [list(map(int, input().split())) for _ in range(S)]

# Output
print(count_danger_castles(N, nazis, S, castles))
