
def can_place_all_disks(n, pillars):
    max_radius = max(pillars)
    max_index = pillars.index(max_radius)
    
    for i in range(max_index, n-1):
        if pillars[i] != max_radius or pillars[i+1] >= max_radius:
            return "NO"
    
    for i in range(max_index, 0, -1):
        if pillars[i] != max_radius or pillars[i-1] >= max_radius:
            return "NO"
    
    return "YES"

# Input
n = int(input())
pillars = list(map(int, input().split()))

# Output
print(can_place_all_disks(n, pillars))