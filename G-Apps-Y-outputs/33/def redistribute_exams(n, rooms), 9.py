
def redistribute_exams(n, rooms):
    total_students = sum(rooms)
    visited = [False] * n
    order = []

    for _ in range(n):
        for i in range(n):
            if not visited[i] and rooms[i] <= total_students:
                order.append(i + 1)
                visited[i] = True
                total_students -= rooms[i]

    if len(order) < n:
        return "impossible"
    else:
        return " ".join(map(str, order))

# Input
n = 4
rooms = [2, 3, 3, 1]

# Output
print(redistribute_exams(n, rooms))
