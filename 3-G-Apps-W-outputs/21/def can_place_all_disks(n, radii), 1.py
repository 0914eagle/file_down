
def can_place_all_disks(n, radii):
    max_radius = max(radii)
    min_radius = min(radii)
    max_index = radii.index(max_radius)
    min_index = radii.index(min_radius)
    
    if max_index < min_index:
        max_index, min_index = min_index, max_index
    
    for i in range(min_index, max_index):
        if radii[i] > radii[i+1]:
            return "NO"
    
    return "YES"

# Input
n = int(input())
radii = list(map(int, input().split()))

# Output
print(can_place_all_disks(n, radii))
