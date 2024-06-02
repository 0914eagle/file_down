
def is_inside_quadrilateral(p1, p2, p3, p4, castle):
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


def count_castles_in_danger(N, nazis, S, castles):
    count = 0
    for i in range(N - 3):
        for j in range(i + 1, N - 2):
            for k in range(j + 1, N - 1):
                for l in range(k + 1, N):
                    p1, p2, p3, p4 = nazis[i], nazis[j], nazis[k], nazis[l]
                    for castle in castles:
                        if is_inside_quadrilateral(p1, p2, p3, p4, castle):
                            count += 1
                            break
    return count


# Read input
N = int(input())
nazis = [tuple(map(int, input().split())) for _ in range(N)]
S = int(input())
castles = [tuple(map(int, input().split())) for _ in range(S)]

# Calculate and output the number of castles in danger
print(count_castles_in_danger(N, nazis, S, castles))
