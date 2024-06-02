
def can_place_all_disks(n, pillars):
    max_radius = max(pillars)
    max_index = pillars.index(max_radius)
    
    if max_index == 0:
        for i in range(1, n):
            if pillars[i] <= pillars[i-1]:
                return "NO"
    elif max_index == n-1:
        for i in range(n-2, -1, -1):
            if pillars[i] <= pillars[i+1]:
                return "NO"
    else:
        for i in range(max_index-1, -1, -1):
            if pillars[i] <= pillars[i+1]:
                return "NO"
        for i in range(max_index+1, n):
            if pillars[i] <= pillars[i-1]:
                return "NO"
    
    return "YES"

# Input
n = int(input())
pillars = list(map(int, input().split()))

# Output
print(can_place_all_disks(n, pillars))
