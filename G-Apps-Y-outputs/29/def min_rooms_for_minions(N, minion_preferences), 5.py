
def min_rooms_for_minions(N, minion_preferences):
    rooms = []
    for preference in minion_preferences:
        assigned = False
        for room in rooms:
            if preference[0] >= room[0] and preference[1] <= room[1]:
                assigned = True
                break
        if not assigned:
            rooms.append(preference)
    
    return len(rooms)

# Input
N = int(input())
minion_preferences = []
for _ in range(N):
    L, U = map(int, input().split())
    minion_preferences.append((L, U))

# Output
print(min_rooms_for_minions(N, minion_preferences))
