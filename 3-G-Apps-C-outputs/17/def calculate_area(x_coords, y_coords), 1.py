
def calculate_area(x_coords, y_coords):
    n = len(x_coords)
    area = 0
    for i in range(n-1):
        area += (x_coords[i] * y_coords[i+1] - x_coords[i+1] * y_coords[i])
    area += (x_coords[n-1] * y_coords[0] - x_coords[0] * y_coords[n-1])
    return abs(area) / 2

def calculate_areas(n, nails, picks):
    x_coords = [nail[0] for nail in nails]
    y_coords = [nail[1] for nail in nails]
    areas = []
    
    for pick in picks:
        if pick == 'L':
            idx = x_coords.index(min(x_coords))
        elif pick == 'R':
            idx = x_coords.index(max(x_coords))
        elif pick == 'U':
            idx = y_coords.index(max(y_coords))
        elif pick == 'D':
            idx = y_coords.index(min(y_coords))
        
        x_coords.pop(idx)
        y_coords.pop(idx)
        areas.append(calculate_area(x_coords, y_coords))
    
    return areas

# Input
n = int(input())
nails = [list(map(int, input().split())) for _ in range(n)]
picks = input().strip()

# Calculate and output areas
areas = calculate_areas(n, nails, picks)
for area in areas:
    print("{:.1f}".format(area))
