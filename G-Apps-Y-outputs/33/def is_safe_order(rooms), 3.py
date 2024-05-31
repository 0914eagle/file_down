
from itertools import permutations

def is_safe_order(rooms):
    n = len(rooms)
    num_exams = sum(rooms)
    exams_pile = list(range(num_exams))

    for i in range(n):
        exams_in_room = rooms[i]
        for j in range(exams_in_room):
            if exams_pile[j] // n == i:
                return False
        exams_pile = exams_pile[exams_in_room:] + exams_pile[:exams_in_room]

    return True

n = int(input())
rooms = list(map(int, input().split()))

found_safe_order = False
for perm in permutations(range(1, n+1)):
    perm = tuple(perm)
    perm_rooms = [rooms[i-1] for i in perm]
    if is_safe_order(perm_rooms):
        print(*perm)
        found_safe_order = True
        break

if not found_safe_order:
    print("impossible")
