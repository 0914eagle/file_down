
import heapq

def calculate_area(nails):
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def get_area(a, b, c):
        return abs(cross_product(a, b, c)) / 2.0

    def remove_nail(nail):
        nails.remove(nail)

    def get_extreme_nail(direction):
        if direction == 'L':
            return min(nails)
        elif direction == 'R':
            return max(nails)
        elif direction == 'U':
            return max(nails, key=lambda x: (-x[1], x[0]))
        elif direction == 'D':
            return min(nails, key=lambda x: (x[1], x[0]))

    areas = []
    for i in range(len(directions)):
        nail = get_extreme_nail(directions[i])
        areas.append(0.0)
        for j in range(len(nails)):
            if j == 0:
                continue
            areas[-1] += get_area(nails[j-1], nails[j], nail)
        remove_nail(nail)

    return areas

# Input
n = int(input())
nails = [tuple(map(int, input().split())) for _ in range(n)]
directions = input().strip()

# Calculate areas
result = calculate_area(nails)

# Output
for area in result:
    print("{:.1f}".format(area))

