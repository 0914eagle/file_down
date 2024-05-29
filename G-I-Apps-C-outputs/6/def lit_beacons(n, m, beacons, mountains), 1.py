
def lit_beacons(n, m, beacons, mountains):
    connected = set()
    
    def is_visible(beacon1, beacon2, mountains):
        x1, y1 = beacon1
        x2, y2 = beacon2
        for peak in mountains:
            peak_x, peak_y, peak_r = peak
            dx = x2 - x1
            dy = y2 - y1
            a = dx*dx + dy*dy
            b = 2*(dx*(x1-peak_x) + dy*(y1-peak_y))
            c = (x1-peak_x)*(x1-peak_x) + (y1-peak_y)*(y1-peak_y) - peak_r*peak_r
            d = b*b - 4*a*c
            if d >= 0:
                return False
        return True
    
    for i in range(n):
        for j in range(i+1, n):
            if is_visible(beacons[i], beacons[j], mountains):
                connected.add((i, j))
                connected.add((j, i))
    
    messages = 0
    visited = set()
    while len(visited) < n:
        messages += 1
        stack = [next(iter(set(range(n)) - visited))]
        while stack:
            beacon = stack.pop()
            visited.add(beacon)
            for neighbor in range(n):
                if neighbor not in visited and (beacon, neighbor) in connected:
                    stack.append(neighbor)
    
    return messages - 1

# Example Input
n = 6  # number of beacons
m = 3  # number of mountain peaks
beacons = [(1, 8), (5, 4), (7, 7), (9, 2), (16, 6), (17, 10)]
mountains = [(4, 7, 2), (6, 3, 1), (12, 6, 3)]

print(lit_beacons(n, m, beacons, mountains))
```
