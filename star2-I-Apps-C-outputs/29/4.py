
import math

def is_in_sight(beacon1, beacon2, mountains):
    dx = beacon2[0] - beacon1[0]
    dy = beacon2[1] - beacon1[1]
    distance = math.sqrt(dx * dx + dy * dy)
    for mountain in mountains:
        dx = mountain[0] - beacon1[0]
        dy = mountain[1] - beacon1[1]
        distance_to_mountain = math.sqrt(dx * dx + dy * dy)
        if distance_to_mountain < mountain[2]:
            return False
    return True

def solve(beacons, mountains):
    visited = set()
    queue = [beacons[0]]
    while queue:
        beacon = queue.pop(0)
        if beacon in visited:
            continue
        visited.add(beacon)
        for other_beacon in beacons:
            if other_beacon == beacon:
                continue
            if is_in_sight(beacon, other_beacon, mountains):
                queue.append(other_beacon)
    return len(visited)

def main():
    n, m = map(int, input().split())
    beacons = []
    for _ in range(n):
        x, y = map(int, input().split())
        beacons.append((x, y))
    mountains = []
    for _ in range(m):
        x, y, r = map(int, input().split())
        mountains.append((x, y, r))
    result = solve(beacons, mountains)
    print(result)

if __name__ == "__main__":
    main()

