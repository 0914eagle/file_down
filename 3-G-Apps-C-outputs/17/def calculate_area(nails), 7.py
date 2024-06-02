
def calculate_area(nails):
    def shoelace_formula(points):
        n = len(points)
        area = 0
        for i in range(n):
            j = (i + 1) % n
            area += points[i][0] * points[j][1] - points[j][0] * points[i][1]
        return abs(area) / 2

    areas = []
    points = sorted(nails)
    for i in range(1, len(points) - 1):
        areas.append(shoelace_formula([points[0], points[i], points[-1]]))
    return areas

N = int(input())
nails = [list(map(int, input().split())) for _ in range(N)]
order = input().strip()

result = calculate_area(nails)
for o in order:
    if o == 'L':
        nails = sorted(nails, key=lambda x: x[0])
    elif o == 'R':
        nails = sorted(nails, key=lambda x: x[0], reverse=True)
    elif o == 'U':
        nails = sorted(nails, key=lambda x: x[1], reverse=True)
    elif o == 'D':
        nails = sorted(nails, key=lambda x: x[1])
    result.append(calculate_area(nails)[0])
    nails = nails[1:]

for area in result:
    print("{:.1f}".format(area))
