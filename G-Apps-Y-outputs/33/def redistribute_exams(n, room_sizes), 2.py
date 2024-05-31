
import itertools

def redistribute_exams(n, room_sizes):
    total_students = sum(room_sizes)
    all_rooms = list(range(1, n + 1))
    
    for perm in itertools.permutations(all_rooms):
        exams_pile = total_students
        visited_rooms = set()
        safe_order = []
        
        for room in perm:
            if exams_pile < room_sizes[room - 1] or room in visited_rooms:
                break
            
            exams_pile -= room_sizes[room - 1]
            visited_rooms.add(room)
            safe_order.append(room)
        
        if len(safe_order) == n:
            return safe_order
        
    return "impossible"

# Input
n = int(input())
room_sizes = list(map(int, input().split()))

# Output
safe_order = redistribute_exams(n, room_sizes)
print(*safe_order)
