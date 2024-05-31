
import itertools

def redistribute_exams(n, rooms):
    total_students = sum(rooms)
    rooms_order = list(range(1, n+1))

    for perm in itertools.permutations(rooms_order):
        exams_pile = list(range(1, total_students+1))
        exams_remaining = len(exams_pile)

        for room in perm:
            room_students = rooms[room-1]
            if exams_remaining < room_students:
                break

            exams_distribution = exams_pile[:room_students]
            exams_pile = exams_pile[room_students:] + exams_distribution
            exams_remaining = len(exams_pile)

        if exams_remaining >= total_students:
            return perm

    return "impossible"

# Input
n = int(input())
rooms = list(map(int, input().split()))

# Output
result = redistribute_exams(n, rooms)
if result == "impossible":
    print("impossible")
else:
    print(*result)
