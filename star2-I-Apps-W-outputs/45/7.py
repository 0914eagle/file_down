
def can_visit_friend(teleports, m):
    current_position = 0
    while current_position < m:
        next_position = current_position
        for teleport in teleports:
            if teleport[0] <= current_position and teleport[1] >= current_position:
                next_position = max(next_position, teleport[1])
        if next_position == current_position:
            return False
        current_position = next_position
    return True

n, m = map(int, input().split())
teleports = []
for _ in range(n):
    teleports.append(list(map(int, input().split())))
if can_visit_friend(teleports, m):
    print("YES")
else:
    print("NO")

