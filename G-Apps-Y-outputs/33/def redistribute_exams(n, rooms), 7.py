
import itertools

def redistribute_exams(n, rooms):
    total_students = sum(rooms)
    all_rooms = list(range(1, n+1))
    safe_orders = list(itertools.permutations(all_rooms))

    for order in safe_orders:
        pile = total_students
        visited_rooms = set()
        for room in order:
            if pile < rooms[room-1] or room in visited_rooms:
                break
            pile += len(visited_rooms) - rooms[room-1]
            visited_rooms.add(room)
        else:
            return order

    return "impossible"

# Input reading
n = int(input())
rooms = list(map(int, input().split()))

# Solve the problem
result = redistribute_exams(n, rooms)
print(result)
