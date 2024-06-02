
import math

def calculate_area(x1, y1, x2, y2):
    return abs(x1*y2 - x2*y1) / 2

def calculate_areas(nails, picks):
    areas = []
    for i in range(len(picks)):
        x_values = [nail[0] for nail in nails]
        y_values = [nail[1] for nail in nails]
        
        if picks[i] == 'L':
            index = x_values.index(min(x_values))
        elif picks[i] == 'R':
            index = x_values.index(max(x_values))
        elif picks[i] == 'U':
            index = y_values.index(max(y_values))
        elif picks[i] == 'D':
            index = y_values.index(min(y_values))
        
        area = 0
        if index == 0:
            area = calculate_area(nails[1][0]-nails[0][0], nails[1][1]-nails[0][1], nails[-1][0]-nails[0][0], nails[-1][1]-nails[0][1])
            nails.pop(0)
        elif index == len(nails)-1:
            area = calculate_area(nails[0][0]-nails[-1][0], nails[0][1]-nails[-1][1], nails[-2][0]-nails[-1][0], nails[-2][1]-nails[-1][1])
            nails.pop()
        else:
            area = calculate_area(nails[index-1][0]-nails[index][0], nails[index-1][1]-nails[index][1], nails[index+1][0]-nails[index][0], nails[index+1][1]-nails[index][1])
            nails.pop(index)
        
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
areas = calculate_areas(nails, picks)

# Output
for area in areas:
    print("{:.1f}".format(area))
