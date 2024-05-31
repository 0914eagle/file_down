
def minimum_rooms_needed(N, minions):
    rooms = []  # List to store the temperature preferences of each room
    for minion in minions:
        assigned = False
        for room in rooms:
            if minion[0] <= room[1] and minion[1] >= room[0]:
                room[0] = max(room[0], minion[0])
                room[1] = min(room[1], minion[1])
                assigned = True
                break
        if not assigned:
            rooms.append([minion[0], minion[1]])
    
    return len(rooms)

# Input processing
N = int(input())
minions = []
for _ in range(N):
    L, U = map(int, input().split())
    minions.append([L, U])

print(minimum_rooms_needed(N, minions))
