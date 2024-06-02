
def is_inside(p1, p2, p3, p4, castle):
    def cross_product(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    def is_on_segment(p1, p2, p3):
        return min(p1[0], p2[0]) <= p3[0] <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= p3[1] <= max(p1[1], p2[1])

    def intersect(p1, p2, p3, p4):
        return cross_product(p1, p2, p3) * cross_product(p1, p2, p4) <= 0 and cross_product(p3, p4, p1) * cross_product(p3, p4, p2) <= 0

    return intersect(p1, p2, p3, p4) and is_on_segment(p1, p2, castle) and is_on_segment(p3, p4, castle)

def count_danger_castles(N, nazis, S, castles):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    for castle in castles:
                        if is_inside(nazis[i], nazis[j], nazis[k], nazis[l], castle):
                            count += 1
                            break
    return count

# Input reading
N = int(input())
nazis = [tuple(map(int, input().split())) for _ in range(N)]
S = int(input())
castles = [tuple(map(int, input().split())) for _ in range(S)]

# Count the number of castles in danger
result = count_danger_castles(N, nazis, S, castles)
print(result)
