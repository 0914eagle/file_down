
def minimum_rooms_needed(N, preferences):
    preferences.sort(key=lambda x: x[0])  # Sort minions' preferences based on lower temperature limit

    rooms = []
    for pref in preferences:
        assigned = False
        for room in rooms:
            if pref[0] > room[-1][1] or pref[1] < room[0][0]:  # If current preference does not overlap with any existing room
                room.append(pref)
                assigned = True
                break
        if not assigned:  # If current preference does not fit in any existing room
            rooms.append([pref])

    return len(rooms)

# Sample Input
N = 3
preferences = [(1, 2), (2, 4), (5, 6)]
print(minimum_rooms_needed(N, preferences))  # Output: 2
