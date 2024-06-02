
import heapq

def calculate_area(nails):
    if len(nails) < 3:
        return []
    
    def area(a, b, c):
        return abs((a[0] - c[0]) * (b[1] - a[1]) - (a[0] - b[0]) * (c[1] - a[1])) / 2.0
    
    result = []
    hull = []
    heapq.heappush(hull, nails[0])
    heapq.heappush(hull, nails[-1])
    
    for i in range(1, len(nails) - 1):
        heapq.heappush(hull, nails[i])
        while len(hull) >= 3:
            if hull[0][0] <= hull[1][0] <= hull[2][0] or hull[0][0] >= hull[1][0] >= hull[2][0] or hull[0][1] <= hull[1][1] <= hull[2][1] or hull[0][1] >= hull[1][1] >= hull[2][1]:
                break
            heapq.heappop(hull)
        
        result.append(area(hull[0], hull[1], hull[2]))
    
    return result

# Input
N = int(input())
nails = [tuple(map(int, input().split())) for _ in range(N)]
directions = input().strip()

# Process input
nail_map = {nails[i]: i for i in range(N)}
sorted_nails = sorted(nails)

result = calculate_area(sorted_nails)

# Output
for direction in directions:
    index = nail_map[sorted_nails.pop(0)]
    del nail_map[nails[index]]
    result.pop(nail_map[nails[index]])
    print("{:.1f}".format(result[nail_map[sorted_nails[0]]]))
