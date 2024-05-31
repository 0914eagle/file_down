
def min_rooms_for_minions(N, preferences):
    intervals = sorted(preferences, key=lambda x: x[0])
    rooms = []
    
    for start, end in intervals:
        assigned = False
        for room in rooms:
            if room[-1][1] < start or room[0][0] > end:
                room.append((start, end))
                assigned = True
                break
        if not assigned:
            rooms.append([(start, end)])
    
    return len(rooms)

# Input processing
N = int(input())
preferences = []
for _ in range(N):
    L, U = map(int, input().split())
    preferences.append((L, U))

# Call the function and print the result
print(min_rooms_for_minions(N, preferences))
