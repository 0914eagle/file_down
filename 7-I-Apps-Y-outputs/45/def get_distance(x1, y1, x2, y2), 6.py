
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def get_closest_hole(x1, y1, holes):
    min_distance = float('inf')
    closest_hole = None
    for hole in holes:
        x2, y2 = hole
        distance = get_distance(x1, y1, x2, y2)
        if distance < min_distance:
            min_distance = distance
            closest_hole = hole
    return closest_hole

def get_escape_hole(x1, y1, x2, y2, holes):
    min_distance = float('inf')
    escape_hole = None
    for hole in holes:
        x2, y2 = hole
        distance = get_distance(x1, y1, x2, y2)
        if distance < min_distance:
            min_distance = distance
            escape_hole = hole
    return escape_hole

def main():
    x1, y1, x2, y2 = [float(i) for i in input().split()]
    holes = []
    for _ in range(int(input())):
        x, y = [float(i) for i in input().split()]
        holes.append((x, y))

    closest_hole = get_closest_hole(x1, y1, holes)
    escape_hole = get_escape_hole(x1, y1, x2, y2, holes)

    if escape_hole == closest_hole:
        print('The gopher can escape through the hole at ({}, {})'.format(*escape_hole))
    else:
        print('The gopher cannot escape.')

if __name__ == '__main__':
    main()

