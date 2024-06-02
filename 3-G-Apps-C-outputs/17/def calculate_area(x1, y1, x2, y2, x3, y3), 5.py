
import math

def calculate_area(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))

def calculate_areas(nails, picks):
    areas = []
    for i in range(len(picks)):
        if picks[i] == 'L':
            areas.append(calculate_area(*nails[i], *nails[i+1], *nails[i+2]))
        elif picks[i] == 'R':
            areas.append(calculate_area(*nails[i+2], *nails[i+1], *nails[i]))
        elif picks[i] == 'U':
            areas.append(calculate_area(*nails[i+2], *nails[i], *nails[i+1]))
        elif picks[i] == 'D':
            areas.append(calculate_area(*nails[i], *nails[i+2], *nails[i+1]))
    return areas

# Input
N = int(input())
nails = [list(map(int, input().split())) for _ in range(N)]
picks = input().strip()

# Calculate areas
areas = calculate_areas(nails, picks)

# Output
for area in areas:
    print("{:.1f}".format(area))
