
def is_inside_quadrilateral(p1, p2, p3, p4, castle):
    def cross_product(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    def is_on_same_side(p1, p2, p3, p4):
        cp1 = cross_product(p3, p4, p1)
        cp2 = cross_product(p3, p4, p2)
        return cp1 * cp2 > 0

    return is_on_same_side(p1, p2, p3, p4) and is_on_same_side(p2, p3, p4, p1) and is_on_same_side(p3, p4, p1, p2)

def count_danger_castles(N, nazis, S, castles):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    for castle in castles:
                        if is_inside_quadrilateral(nazis[i], nazis[j], nazis[k], nazis[l], castle):
                            count += 1
                            break
    return count

# Read input
N = int(input())
nazis = [list(map(int, input().split())) for _ in range(N)]
S = int(input())
castles = [list(map(int, input().split())) for _ in range(S)]

# Calculate and print output
print(count_danger_castles(N, nazis, S, castles))
