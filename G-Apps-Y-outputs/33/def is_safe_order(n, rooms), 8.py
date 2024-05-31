
def is_safe_order(n, rooms):
    total_students = sum(rooms)
    visited = set()
    order = []

    for _ in range(n):
        next_room = None
        for i in range(n):
            if i not in visited and (next_room is None or rooms[i] < rooms[next_room]):
                next_room = i

        if next_room is None or rooms[next_room] > total_students // 2:
            return "impossible"

        visited.add(next_room)
        total_students -= rooms[next_room]
        order.append(next_room + 1)

    return order

# Input
n = int(input())
rooms = list(map(int, input().split()))

# Output
result = is_safe_order(n, rooms)
print(*result if result != "impossible" else result)
