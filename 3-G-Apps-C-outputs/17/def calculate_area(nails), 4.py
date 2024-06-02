
def calculate_area(nails):
    area = 0
    for i in range(len(nails) - 1):
        area += nails[i][0] * nails[i + 1][1] - nails[i + 1][0] * nails[i][1]
    area += nails[-1][0] * nails[0][1] - nails[0][0] * nails[-1][1]
    return abs(area) / 2

def calculate_areas(n, nails, picks):
    areas = []
    for i in range(n - 2):
        pick = picks[i]
        if pick == 'L':
            nails.sort(key=lambda x: x[0])
        elif pick == 'R':
            nails.sort(key=lambda x: x[0], reverse=True)
        elif pick == 'U':
            nails.sort(key=lambda x: x[1], reverse=True)
        elif pick == 'D':
            nails.sort(key=lambda x: x[1])
        
        areas.append(calculate_area(nails))
        nails.remove(nails[0])
    
    return areas

# Input
n = int(input())
nails = []
for _ in range(n):
    x, y = map(int, input().split())
    nails.append((x, y))
picks = input().strip()

# Calculate and output areas
areas = calculate_areas(n, nails, picks)
for area in areas:
    print("{:.1f}".format(area))
