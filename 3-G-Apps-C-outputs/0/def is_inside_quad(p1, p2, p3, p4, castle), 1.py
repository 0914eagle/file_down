
def is_inside_quad(p1, p2, p3, p4, castle):
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    def on_segment(p, q, r):
        if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
                q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
            return True
        return False

    def do_intersect(p1, q1, p2, q2):
        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)

        if o1 != o2 and o3 != o4:
            return True

        if o1 == 0 and on_segment(p1, p2, q1):
            return True
        if o2 == 0 and on_segment(p1, q2, q1):
            return True
        if o3 == 0 and on_segment(p2, p1, q2):
            return True
        if o4 == 0 and on_segment(p2, q1, q2):
            return True

        return False

    return (do_intersect(p1, p2, p3, castle) or
            do_intersect(p2, p3, p4, castle) or
            do_intersect(p3, p4, p1, castle) or
            do_intersect(p4, p1, p2, castle))


def count_danger_castles(N, nazi_troops, S, soviet_castles):
    count = 0
    for castle in soviet_castles:
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    for l in range(k + 1, N):
                        if is_inside_quad(nazi_troops[i], nazi_troops[j], nazi_troops[k], nazi_troops[l], castle):
                            count += 1
                            break
    return count


# Read input
N = int(input())
nazi_troops = [tuple(map(int, input().split())) for _ in range(N)]
S = int(input())
soviet_castles = [tuple(map(int, input().split())) for _ in range(S)]

# Count the number of castles in danger
result = count_danger_castles(N, nazi_troops, S, soviet_castles)
print(result)
