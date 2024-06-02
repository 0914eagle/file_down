
def is_inside_quad(p1, p2, p3, p4, castle):
    def cross_product(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    def is_on_segment(p1, p2, p3):
        return min(p1[0], p2[0]) <= p3[0] <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= p3[1] <= max(p1[1], p2[1])

    def segments_intersect(p1, p2, p3, p4):
        d1 = cross_product(p3, p4, p1)
        d2 = cross_product(p3, p4, p2)
        d3 = cross_product(p1, p2, p3)
        d4 = cross_product(p1, p2, p4)
        if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
            return True
        if d1 == 0 and is_on_segment(p3, p4, p1):
            return True
        if d2 == 0 and is_on_segment(p3, p4, p2):
            return True
        if d3 == 0 and is_on_segment(p1, p2, p3):
            return True
        if d4 == 0 and is_on_segment(p1, p2, p4):
            return True
        return False

    return segments_intersect(p1, p2, p3, p4) or segments_intersect(p1, p3, p2, p4) or segments_intersect(p1, p4, p2, p3)

def count_dangerous_castles(N, nazis, S, castles):
    count = 0
    for i in range(S):
        for j in range(N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    if is_inside_quad(nazis[j], nazis[k], nazis[l], nazis[i], castles[i]):
                        count += 1
                        break
    return count

# Read input
N = int(input())
nazis = [tuple(map(int, input().split())) for _ in range(N)]
S = int(input())
castles = [tuple(map(int, input().split())) for _ in range(S)]

# Calculate and output the number of castles in danger
print(count_dangerous_castles(N, nazis, S, castles))
