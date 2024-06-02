
import math

def calculate_area(nails):
    x_coords = [nail[0] for nail in nails]
    y_coords = [nail[1] for nail in nails]
    
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)
    
    return (max_x - min_x) * (max_y - min_y)

def calculate_areas(n, nails, picks):
    areas = []
    
    for i in range(n - 2):
        pick = picks[i]
        remaining_nails = [nail for nail in nails if nail != picks[i]]
        area = calculate_area(remaining_nails)
        areas.append(area)
    
    return areas

# Input
n = int(input())
nails = []
for _ in range(n):
    x, y = map(int, input().split())
    nails.append((x, y))
picks = input().strip()

# Calculate areas
areas = calculate_areas(n, nails, picks)

# Output
for area in areas:
    print("{:.1f}".format(area))
