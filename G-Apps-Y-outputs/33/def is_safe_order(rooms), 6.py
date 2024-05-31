
import itertools

def is_safe_order(rooms):
    total_students = sum(rooms)
    num_rooms = len(rooms)
    
    for permutation in itertools.permutations(range(num_rooms)):
        pile = []
        visited_rooms = set()
        current_room = 0
        
        while len(pile) < total_students:
            if current_room in visited_rooms:
                break
            
            visited_rooms.add(current_room)
            num_students = rooms[current_room]
            if len(pile) + num_students > total_students:
                break
            
            for _ in range(num_students):
                pile.append(current_room)
            
            current_room = permutation[current_room]
        
        if len(pile) == total_students:
            return permutation
    
    return "impossible"

# Read input
n = int(input())
rooms = list(map(int, input().split()))

# Find safe order
safe_order = is_safe_order(rooms)

if safe_order == "impossible":
    print("impossible")
else:
    print(" ".join(str(room + 1) for room in safe_order))
