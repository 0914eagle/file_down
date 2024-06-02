
def can_place_all_disks(n, radii):
    max_radius = max(radii)
    min_radius = min(radii)

    max_idx = radii.index(max_radius)
    min_idx = radii.index(min_radius)

    if (max_idx == min_idx + 1) or (min_idx == max_idx + 1):
        return "YES"
    else:
        return "NO"

# Input
n = int(input())
radii = list(map(int, input().split()))

# Output
print(can_place_all_disks(n, radii))
