
import heapq

def calculate_area(nails):
    def area(a, b, c):
        return abs((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])) / 2.0

    def remove_nail(nail, left, right, top, bottom):
        left.remove(nail)
        right.remove(nail)
        top.remove(nail)
        bottom.remove(nail)

    left = list(nails)
    right = list(nails)
    top = list(nails)
    bottom = list(nails)

    heapq.heapify(left)
    heapq.heapify(right, lambda x: -x)
    heapq.heapify(top, lambda x: (-x[1], x[0]))
    heapq.heapify(bottom, lambda x: (x[1], x[0]))

    result = []
    for move in moves:
        if move == 'L':
            nail = heapq.heappop(left)
        elif move == 'R':
            nail = heapq.heappop(right)
        elif move == 'U':
            nail = heapq.heappop(top)
        elif move == 'D':
            nail = heapq.heappop(bottom)

        result.append(area(left[0], right[0], top[0]))
        remove_nail(nail, left, right, top, bottom)

    return result

# Input
n = int(input())
nails = [list(map(int, input().split())) for _ in range(n)]
moves = input().strip()

# Calculate areas
areas = calculate_area(nails)

# Output
for area in areas:
    print("{:.1f}".format(area))
